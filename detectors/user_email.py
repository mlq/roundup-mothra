from roundup import i18n
from validate_email import validate_email

def audit_email(db, cl, nodeid, newvalues):
  if newvalues.has_key('address'):
    address = newvalues['address']
    if not validate_email(address):
      raise ValueError(i18n.gettext("Email address %s is invalid"), address)

def init(db):
  db.user.audit('set',    audit_email)
  db.user.audit('create', audit_email)
