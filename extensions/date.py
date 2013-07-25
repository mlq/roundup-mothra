import datetime

def get_date():
  now = datetime.datetime.now()
  return now.strftime("%Y-%m-%d")

def init(instance):
  instance.registerUtil('get_date', get_date)
