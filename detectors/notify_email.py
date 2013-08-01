from roundup import roundupdb

def notify_subscriber(db, cl, nodeid, oldvalues):
  change_note = cl.generateCreateNote(nodeid)

  # send a copy to the nosy list
  for msgid in cl.get(nodeid, 'messages'):
    try:
      mails = []
      subscribers = db.user.filter(None, {'subscribe' : 1})
      for user_id in subscribers:
        address = db.user.get(user_id, 'address')
        mails.append(address)

      if len(mails) != 0:
        cl.send_message(nodeid, msgid, change_note, mails)
    except roundupdb.MessageSendError as message:
      raise roundupdb.DetectorError(message)

def init(db):
  db.issue.react('create', notify_subscriber)
