################################################################################
# TRACKER SCHEMA
################################################################################
#
# The schema for the mothra template to provide support for projects, version
# and milestone management
#
# All Class'es automatically have the following properties:
#   creation = Date()
#   activity = Date()
#   creator = Link('user')
#   actor = Link('user')
#
# All FileClass'es automatically gets this property in addition to the Class
# ones:
#   content = String() [saved to disk in <tracker home>/db/files/]
#   type = String()    [MIME type of the content, default 'text/plain']
#
# All IssueClass'es automatically gets these properties in addition to the Class
# ones:
#   title = String()
#   messages = Multilink("msg")
#   files = Multilink("file")
#   nosy = Multilink("user")
#   superseder = Multilink("issue")

# Project
#   Minimalistic representation of a project consisting out of its name, a
#   description field as well as a link to its website
project = Class(db, "project",
    name        = String(),
    description = String(),
    homepage    = String()
  )
project.setkey("name")

# Version
#   A version is represented by a name and linked to a project. Therefore
#   multiple project can have the same version name.
version = Class(db, "version",
    name    = String(),
    project = Link('project')
  )

# Milestone
#   A milestone is represented by a name and linked to a project.
milestone = Class(db, "milestone",
    name    = String(),
    project = Link('project')
  )

# Priorities
#   Priorities are used to sub-divide the issues into their relevance to be
#   ressolved
priority = Class(db, "priority",
    name  = String(),
    order = Number()
  )
priority.setkey("name")

# Statuses
#   The status represents the current state of an issue
status = Class(db, "status",
    name  = String(),
    order = Number()
  )
status.setkey("name")

# Issue type
issue_type = Class(db, "issue_type",
    name  = String(),
    order = Number()
  )
issue_type.setkey("name")

# Resolution
resolution = Class(db, "resolution",
    name  = String(),
    order = Number()
  )
resolution.setkey("name")

# User-defined saved searches
#   A user can save custom search queries
query = Class(db, "query",
    klass       = String(),
    name        = String(),
    url         = String(),
    private_for = Link('user')
  )

# User
#   A user of the tracker
user = Class(db, "user",
    username = String(),
    password = Password(),
    address  = String(),
    realname = String(),
    website  = String(),
    queries  = Multilink('query'),
    roles    = String(), # comma-separated string of Role names
    timezone = String()
  )
user.setkey("username")

# Message
#   Represents a message of an issue
msg = FileClass(db, "msg",
    author     = Link("user", do_journal = 'no'),
    recipients = Multilink("user", do_journal = 'no'),
    date       = Date(),
    files      = Multilink("file"),
    messageid  = String(),
    inreplyto  = String()
  )

# File
#   Represents a file that can be uploaded and attached to a message
file = FileClass(db, "file",
    name = String()
  )

# Issue
#   Represents an issue in the tracker
issue = IssueClass(db, "issue",
    issue_type = Link("issue_type"),
    assignedto = Link("user"),
    priority   = Link("priority"),
    resolution = Link("resolution"),
    project    = Link("project"),
    milestone  = Link("milestone"),
    version    = Link("version"),
    status     = Link("status")
  )

################################################################################
# TRACKER SECURITY SETTINGS
################################################################################
#
# See the configuration and customisation document for information about
# security setup.

# GENERAL
#
# User can register a new user
db.security.addPermission(name='Register', klass='user', 
    description='User is allowed to register new user')

# REGULAR USERS
#
# Give the regular users access to the web and email interface
db.security.addPermissionToRole('User', 'Web Access')
db.security.addPermissionToRole('User', 'Email Access')

# Assign the access and edit Permissions for issue, file and message
# to regular users now
for cl in 'issue', 'file', 'msg':
    db.security.addPermissionToRole('User', 'View', cl)
    db.security.addPermissionToRole('User', 'Edit', cl)
    db.security.addPermissionToRole('User', 'Create', cl)

# Allow to view the issue properties
for cl in 'issue_type', 'priority', 'resolution', 'status', 'project', \
    'milestone', 'version':
    db.security.addPermissionToRole('User', 'View', cl)

# Allow users to view the profile of other users
db.security.addPermissionToRole('User', 'View', 'user')

# Users can only edit their own profile
def own_record(db, userid, itemid):
    return userid == itemid

p = db.security.addPermission(name='Edit', klass='user', check=own_record,
    properties=('username', 'password', 'address', 'realname', 'website',
        'organisation', 'queries', 'timezone'),
    description="User is allowed to edit their own user details")
db.security.addPermissionToRole('User', p)

# Users should be able to edit and view their own queries. They should also
# be able to view any marked as not private. They should not be able to
# edit others' queries, even if they're not private
def view_query(db, userid, itemid):
    private_for = db.query.get(itemid, 'private_for')
    if not private_for:
      return True
    return userid == private_for

def edit_query(db, userid, itemid):
    return userid == db.query.get(itemid, 'creator')

p = db.security.addPermission(name='View', klass='query', check=view_query,
    description="User is allowed to view their own and public queries")
db.security.addPermissionToRole('User', p)

p = db.security.addPermission(name='Search', klass='query')
db.security.addPermissionToRole('User', p)

p = db.security.addPermission(name='Edit', klass='query', check=edit_query,
    description="User is allowed to edit their queries")
db.security.addPermissionToRole('User', p)

p = db.security.addPermission(name='Retire', klass='query', check=edit_query,
    description="User is allowed to retire their queries")
db.security.addPermissionToRole('User', p)

p = db.security.addPermission(name='Create', klass='query',
    description="User is allowed to create queries")
db.security.addPermissionToRole('User', p)


# ANONYMOUS USER PERMISSIONS
#
# Let anonymous users access the web interface. Note that almost all
# trackers will need this Permission. The only situation where it's not
# required is in a tracker that uses an HTTP Basic Authenticated front-end.
db.security.addPermissionToRole('Anonymous', 'Web Access')

# Allow anonymous users to register
db.security.addPermissionToRole('Anonymous', 'Register', 'user')

# Allow anonymous users access to view issues (and the related items)
for cl in 'issue', 'file', 'msg', 'issue_type', 'priority', 'resolution', \
    'status', 'project', 'milestone', 'version':
    db.security.addPermissionToRole('Anonymous', 'View', cl)

# vim: set filetype=python sts=2 sw=2
