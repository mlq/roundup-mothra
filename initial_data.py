# -*- coding: utf-8 -*-

from roundup import password, date

# Create admin and anonymous user
user = db.getclass('user')
user.create(username="admin", password=adminpw,
    address=admin_email, roles='Admin')
user.create(username="anonymous", roles='Anonymous')

# Create default priorities
priority = db.getclass('priority')
priority.create(name = 'critical', order = '1')
priority.create(name = 'high',     order = '2')
priority.create(name = 'normal',   order = '3')
priority.create(name = 'low',      order = '4')

# Create default statuses
status = db.getclass('status')
status.create(name = 'unread', order      = '1')
status.create(name = 'confirmed', order   = '2')
status.create(name = 'deferred', order    = '3')
status.create(name = 'feedback', order    = '4')
status.create(name = 'in-progress', order = '5')
status.create(name = 'testing', order     = '6')
status.create(name = 'resolved', order    = '7')

# Create default issue types
issue_type = db.getclass('issue_type')
issue_type.create(name = 'crash',           order = '1')
issue_type.create(name = 'compile error',   order = '2')
issue_type.create(name = 'resource usage',  order = '3')
issue_type.create(name = 'security',        order = '4')
issue_type.create(name = 'behavior',        order = '5')
issue_type.create(name = 'performance',     order = '6')
issue_type.create(name = 'feature request', order = '7')

# Create default resolution possibilities
resolution = db.getclass('resolution')
resolution.create(name = 'accepted',     order = '1')
resolution.create(name = 'duplicate',    order = '2')
resolution.create(name = 'fixed',        order = '3')
resolution.create(name = 'invalid',      order = '4')
resolution.create(name = 'later',        order = '5')
resolution.create(name = 'out of date',  order = '6')
resolution.create(name = 'postponed',    order = '7')
resolution.create(name = 'rejected',     order = '8')
resolution.create(name = 'remind',       order = '9')
resolution.create(name = 'wont fix',     order = '10')
resolution.create(name = 'works for me', order = '11')
