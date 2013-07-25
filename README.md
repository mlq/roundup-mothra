roundup-mothra
==============

roundup-mothra is a template for the [Roundup Issue Tracker](http://www.roundup-tracker.org/) issue-tracking system that provides additional functionality like project, version and milestone management. It builds upon the [Twitter Bootstrap](http://twitter.github.io/bootstrap) framework and uses the iconic font [Font Awesome](http://fortawesome.github.io/Font-Awesome) to provide an responsive, user-friendly interface. Its intention is to provide a functional and user-friendly bug tracking platform that covers those features that developers or small organizations could need.

Features
--------

  * Bug tracking
  * Project issue management
  * Version management for projects
  * Milestones management projects
  * Conventional and wise default values
  * Responsive design for either mobile, tablet or desktop with [Twitter Bootstrap](http://twitter.github.io/bootstrap) (v3.0.0)
  * [Jinja2](http://jinja.pocoo.org/) templates
  * Built with [LESS](http://lesscss.org)
  * [Font Awesome](http://fortawesome.github.io/Font-Awesome) icons (v2.3.1)

Dependencies
------------

  * [python2-validate_email](http://pypi.python.org/pypi/validate_email)
  * [python2-pytz](http://pypi.python.org/pypi/pytz)

Installation
------------

Adjust the `domain` and `host` values in _mail_ as well as `web` in the
_tracker_ section in the config.ini file accordingly to your setup.
