from roundup import i18n

def audit_roles(db, cl, nodeid, newvalues):
  new_roles = newvalues.get('roles')
  if new_roles:
    for role in [r.lower().strip() for r in newroles.split(',')]:
      if role and not db.security.role.has_key(role):
        raise ValueError(i18n.gettext("Role %s does not exist", role))

def init(db):
  db.user.audit('set',    audit_roles)
  db.user.audit('create', audit_roles)
