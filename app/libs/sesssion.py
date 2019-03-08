from flask import session, current_app as app, redirect
from functools import wraps

LOGIN_KEY = 'login_info'

def login(info):
  session[LOGIN_KEY] = info

def logout():
  session.pop(LOGIN_KEY)

def get_login_info():
  return session.get(LOGIN_KEY)

def check_login(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    if not (LOGIN_KEY in session):
      return redirect('/')

    return f(*args, **kwargs)

  return decorator

