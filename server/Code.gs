/**
 * Ownership study — 팀 서버 (Google Apps Script, 스프레드시트에 연결된 스크립트)
 *
 * 하는 일
 *  - ping   : 팀 코드 확인 → OpenAI 키(스크립트 속성에만 저장)와 현재 상태를 돌려줌
 *  - assign : 참가자 번호(P01…, 테스트 T01…)와 창작 경험 층별 배정 칸 순번을 한 곳에서 나눠 줌 (동시 요청은 잠금으로 순서대로)
 *  - save   : 완료 세션 1행을 'sessions' 시트에 저장(같은 session_id면 덮어씀) + 이미지 포함 JSON을 드라이브 폴더에 저장
 *
 * 스크립트 속성 (프로젝트 설정 → 스크립트 속성):  OPENAI_API_KEY, TEAM_CODE
 * 배포: 배포 → 새 배포 → 유형 '웹 앱' → 실행 사용자 '나', 액세스 권한 '모든 사용자'
 */

function doPost(e) {
  var req;
  try { req = JSON.parse(e.postData.contents); } catch (x) { return out_({ ok: false, error: '잘못된 요청' }); }
  var P = PropertiesService.getScriptProperties();
  var code = P.getProperty('TEAM_CODE');
  if (!code || req.code !== code) return out_({ ok: false, error: '팀 코드가 맞지 않습니다.' });
  try {
    if (req.action === 'ping') return out_({ ok: true, key: P.getProperty('OPENAI_API_KEY') || '', status: status_() });
    if (req.action === 'assign') return out_(assign_(req));
    if (req.action === 'save') return out_(save_(req));
    return out_({ ok: false, error: '알 수 없는 요청: ' + req.action });
  } catch (err) {
    return out_({ ok: false, error: String((err && err.message) || err) });
  }
}

function doGet() { return out_({ ok: true, service: 'ownership-study' }); }

function out_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function pad_(n) { return n < 10 ? '0' + n : String(n); }

function state_() {
  var raw = PropertiesService.getScriptProperties().getProperty('STATE');
  return raw ? JSON.parse(raw) : { P: 0, T: 0, E: 0, N: 0 };
}

function status_() {
  var s = state_(), sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('sessions');
  return { nextP: 'P' + pad_(s.P + 1), assignedP: s.P, slotsUsed: { E: s.E, N: s.N }, saved: sh ? Math.max(0, sh.getLastRow() - 1) : 0 };
}

function sheet_(name, header) {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), sh = ss.getSheetByName(name);
  if (!sh) { sh = ss.insertSheet(name); if (header) sh.appendRow(header); sh.setFrozenRows(1); }
  return sh;
}

function assign_(req) {
  var lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    var P = PropertiesService.getScriptProperties(), s = state_();
    var st = req.stratum === 'E' ? 'E' : 'N', pid, slotIndex = s[st];
    if (req.test) { s.T += 1; pid = 'T' + pad_(s.T); }            // 테스트: 배정 칸을 쓰지 않음
    else { s.P += 1; pid = 'P' + pad_(s.P); s[st] += 1; }          // 본실험: 그 층의 다음 칸 사용
    P.setProperty('STATE', JSON.stringify(s));
    sheet_('assignments', ['time', 'pid', 'is_test', 'stratum', 'slot_index', 'station', 'session_id'])
      .appendRow([new Date(), pid, req.test ? 1 : 0, st, slotIndex, req.station || '', req.sessionId || '']);
    return { ok: true, pid: pid, slotIndex: slotIndex };
  } finally { lock.releaseLock(); }
}

// 참가자가 쓴 글이 수식으로 해석되지 않도록
function cell_(v) {
  if (v === null || v === undefined) return '';
  if (typeof v === 'string' && /^[=+\-@]/.test(v)) return "'" + v;
  return v;
}

function save_(req) {
  var row = req.row || {};
  if (!row.session_id) return { ok: false, error: 'session_id 없음' };
  var lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    var sh = sheet_('sessions');
    var header = sh.getLastColumn() ? sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0].filter(String) : [];
    var missing = Object.keys(row).filter(function (k) { return header.indexOf(k) < 0; });
    if (missing.length) { header = header.concat(missing); sh.getRange(1, 1, 1, header.length).setValues([header]); }
    var vals = header.map(function (k) { return cell_(row[k]); });
    var idCol = header.indexOf('session_id') + 1, target = -1;
    if (sh.getLastRow() > 1) {
      var ids = sh.getRange(2, idCol, sh.getLastRow() - 1, 1).getValues();
      for (var i = 0; i < ids.length; i++) if (String(ids[i][0]) === String(row.session_id)) { target = i + 2; break; }
    }
    if (target > 0) sh.getRange(target, 1, 1, vals.length).setValues([vals]);
    else sh.appendRow(vals);
  } finally { lock.releaseLock(); }
  if (req.session) {
    var folder = folder_(), name = row.session_id + '.json', old = folder.getFilesByName(name);
    while (old.hasNext()) old.next().setTrashed(true);
    folder.createFile(name, JSON.stringify(req.session), 'application/json');
  }
  return { ok: true };
}

function folder_() {
  var P = PropertiesService.getScriptProperties(), id = P.getProperty('FOLDER_ID');
  if (id) { try { return DriveApp.getFolderById(id); } catch (e) {} }
  var f = DriveApp.createFolder('ownership-study 세션 원본 (이미지 포함 JSON)');
  P.setProperty('FOLDER_ID', f.getId());
  return f;
}

/** 처음 한 번 실행: 권한 승인 + 시트·폴더 만들기 */
function setup() {
  sheet_('sessions');
  sheet_('assignments', ['time', 'pid', 'is_test', 'stratum', 'slot_index', 'station', 'session_id']);
  folder_();
  Logger.log('준비 완료. 상태: ' + JSON.stringify(status_()));
}

/** 본실험 시작 직전에만: 번호·배정 카운터를 0으로 (시트 데이터는 지우지 않음) */
function resetCounters() {
  PropertiesService.getScriptProperties().deleteProperty('STATE');
  Logger.log('카운터 초기화: 다음 번호 P01');
}
