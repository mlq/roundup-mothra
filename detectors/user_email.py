from roundup import i18n
from validate_email import validate_email

validate_email = True
verify_email = True

def get_email_addresses(user):
  if user.has_key('address'):
    yield user['address']
  if user.get('alternate_addresses', None):
    for address in user['alternate_addresses'].split('\n'):
      yield address

def audit_email(db, cl, nodeid, newvalues):
  if validate_email:
    for address in get_email_addresses(newvalues):
      if not validate_email(address, verify=verify_email):
        raise ValueError(i18n.gettext("Email address %s is invalid", address))

      user_main = db.user.stringFind(address=address)
      user_other = [u for u in db.user.filter(None, {'alternate_addresses' : address}) if u != nodeid]
      if user_main or user_other:
        raise ValueError(i18n.gettext("Email address %s is already in use", address))

def init(db):
  db.user.audit('set',    audit_email)
  db.user.audit('create', audit_email)
