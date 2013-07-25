from roundup import i18n

def audit_version(db, cl, nodeid, newvalues):
    project = None
    version = None

    if nodeid is not None:
      project = cl.get(nodeid, 'project')
      version = cl.get(nodeid, 'version')

    if newvalues.has_key('version'):
        version = newvalues['version']
    if newvalues.has_key('project'):
        project = newvalues['project']

    if not version:
        return

    if not project:
        raise ValueError(i18n.gettext("Required property 'project' has not been defined."))

    ok = False
    for vid in db.version.list():
        if vid == version:
            prj = db.version.get(vid, 'project')
            if project == prj:
                ok = True

    if not ok:
        raise ValueError(i18n.gettext("Given version does not match project"))

def audit_milestone(db, cl, nodeid, newvalues):
    project = None
    milestone = None

    if nodeid is not None:
      project = cl.get(nodeid, 'project')
      milestone = cl.get(nodeid, 'milestone')

    if newvalues.has_key('milestone'):
        milestone = newvalues['milestone']
    if newvalues.has_key('project'):
        project = newvalues['project']

    if not milestone:
        return

    if not project:
        raise ValueError(i18n.gettext("Required property 'project' has not been defined."))

    ok = False
    for vid in db.milestone.list():
        if vid == milestone:
            prj = db.milestone.get(vid, 'project')
            if project == prj:
                ok = True

    if not ok:
        raise ValueError(i18n.gettext("Given milestone does not match project"))

def init(db):
    db.issue.audit('set', audit_version)
    db.issue.audit('create', audit_version)
    db.issue.audit('set', audit_milestone)
    db.issue.audit('create', audit_version)
