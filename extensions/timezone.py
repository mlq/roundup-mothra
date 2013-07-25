import pytz

def get_timezones():
  return pytz.common_timezones

def init(instance):
  instance.registerUtil('get_timezones', get_timezones)
