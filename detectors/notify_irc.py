import os

file = '/tmp/fifoirc-pwmt'

def tracker_url(db):
  return str(db.config.options[('tracker', 'web')]) + "/"

def onset(db, cl, nodeid, values):
  user  = db.user.get(db.getuid(), 'username')
  title = db.issue.get( nodeid, 'title')
  url   = tracker_url(db) + "issue" + nodeid

  msg = '[bug tracker] [#' + nodeid + '] "' + title + '" (' + url + ') was updated by ' + user;
  os.system("echo '" + msg + "' > " + file)

def oncreate(db, cl, nodeid, values):
  user  = db.user.get(db.getuid(), 'username')
  title = db.issue.get(nodeid, 'title')
  url  = tracker_url(db) + "issue" + nodeid

  msg = '[bug tracker] [#' + nodeid + '] "' + title + '" (' + url + ') was created by ' + user;
  os.system("echo '" + msg + "' > " + file)

def init(db):
  db.issue.react('set',    onset)
  db.issue.react('create', oncreate)
