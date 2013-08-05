from roundup.mailgw import parseContent

def generate_summary(db, cl, nodeid, newvalues):
  if not newvalues.has_key('content') or newvalues.has_key('summary'):
    return

  summary, content = parseContent(newvalues['content'], config=db.config)
  newvalues['summary'] = summary

def init(db):
  db.msg.audit('create', generate_summary)
