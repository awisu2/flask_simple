from flask import Blueprint, current_app as app, session, redirect, request, flash
from app.libs.template import create_template

BP_URL_PREFIX='/'
BP_NAME=BP_URL_PREFIX
bp = Blueprint(BP_NAME, __name__, url_prefix=BP_URL_PREFIX)

LOGIN_KEY = 'user_id'

@bp.route('/', methods=['GET'])
def index():
  # login info
  user_id = session[LOGIN_KEY] if LOGIN_KEY in session else ''
  app.logger.debug(user_id)
  return create_template('index.html', app, title='', user_id=user_id)

@bp.route('/login', methods=['POST'])
def login():
  login_key = request.form.get(LOGIN_KEY)
  if login_key:
    session[LOGIN_KEY] = login_key
  else:
    # エラーメッセージの登録
    flash('なにか名前を入力してください')

  return redirect('/')

@bp.route('/logout', methods=['GET'])
def logout():
  session.pop(LOGIN_KEY)
  return redirect('/')
