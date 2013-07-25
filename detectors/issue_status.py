def audit_status(db, cl, nodeid, newvalues):
  if not newvalues.has_key('messages'):
    return
  if newvalues['messages'] == cl.get(nodeid, 'messages'):
    return

  try:
    feedback = db.status.lookup('feedback')
  except KeyError:
    return

  current_status = cl.get(nodeid, 'status')

  if newvalues.has_key('status'):
    return

  inactive_states = []
  for state in 'unread resolved deferred'.split():
    try:
      inactive_states.append(db.status.lookup(state))
    except KeyError:
      pass

  if current_status in inactive_states:
    newvalues['status'] = feedback

def set_status(db, cl, nodeid, newvalues):
  if newvalues.has_key('status') and newvalues['status']:
      return

  try:
    unread = db.status.lookup('unread')
  except KeyError:
    return

  newvalues['status'] = unread

def init(db):
  db.issue.audit('set',    audit_status)
  db.issue.audit('create', set_status)
