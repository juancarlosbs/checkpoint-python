

def init():
  global storage
  global correct_password
  global given_password
  global is_authenticated
  global authentication_tries
  global max_authentication_tries_allowed

  storage = []
  correct_password = ('yN1825*a')
  given_password = None
  is_authenticated = False
  authentication_tries = 0
  max_authentication_tries_allowed = (3)