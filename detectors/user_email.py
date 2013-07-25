from roundup import i18n
from validate_email import validate_email

def audit_email(db, cl, nodeid, newvalues):
  if user.has_key('address'):
    if not validate_email(user['address']):
      raise ValueError(i18n.gettext("Email address %s is invalid", user['address']))

  user_main = db.user.stringFind(address=address)
  user_other = [u for u in db.user.filter(None, {'alternate_addresses' : address}) if u != nodeid]
  if user_main or user_other:
    raise ValueError(i18n.gettext("Email address %s is already in use", address))

def init(db):
  db.user.audit('set',    audit_email)
  db.user.audit('create', audit_email)
