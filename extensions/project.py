from __future__ import division

import os
import sys
import re

from roundup import date, hyperdb
from roundup.cgi.actions import Action
from roundup.cgi.actions import EditCommon
from roundup.cgi import exceptions

def flot_data_issues_status(issues):
  status = {}
  for issue in issues:
    try:
      status[str(issue.status)] += 1
    except KeyError:
      status[str(issue.status)] = 1

  flot_data = ""
  for name in status:
    flot_data += '{ label: "' + name + '",'
    if str(name) == "resolved":
      flot_data += 'color: ' + "'green',"
    flot_data += 'data: ' + str(status[name]) + '},'

  return flot_data[:-1]

def flot_data_issues_type(issues):
  types = {}
  for issue in issues:
    try:
      types[str(issue.issue_type)] += 1
    except KeyError:
      types[str(issue.issue_type)] = 1

  flot_data = ""
  for name in types:
    flot_data += '{ label: "' + name + '",'
    flot_data += 'data: ' + str(types[name]) + '},'

  return flot_data[:-1]

def project_get_issues_by_milestone(project, milestone):
  L = []
  for issue in db.issues.list():
    if issue.project == project and issue.milestone == milestone:
      L.append(issue)

def project_milestone_get_progress(issues):
  if len(issues) == 0:
    return 0.0

  done = 0.0
  for issue in issues:
    if issue.status.plain() == 'in-progress':
      done += 1

  return int(round((done / len(issues)) * 100));

def project_milestone_get_done(issues):
  if len(issues) == 0:
    return 0.0

  done = 0.0
  for issue in issues:
    if issue.status.plain() == 'resolved':
      done += 1

  return int(round((done / len(issues)) * 100));

def init(instance):
    #Methods used by the workpackages
    instance.registerUtil('project_flot_status', flot_data_issues_status)
    instance.registerUtil('project_flot_type', flot_data_issues_type)
    instance.registerUtil('project_get_issues_by_milestone', project_get_issues_by_milestone)
    instance.registerUtil('project_milestone_get_done', project_milestone_get_done)
    instance.registerUtil('project_milestone_get_progress', project_milestone_get_progress)

    #db = instance.open('admin')

#SHA: 4c7a4c3f90bac5119d291c1774c06c3fc2e12d6a
