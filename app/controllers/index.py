from flask import Blueprint, current_app as app, redirect, request, flash
from app.libs.template import create_template
from app.libs.sesssion import login as session_login, logout as session_logout, check_login, get_login_info

BP_URL_PREFIX = '/'
BP_NAME = BP_URL_PREFIX
bp = Blueprint(BP_NAME, __name__, url_prefix=BP_URL_PREFIX)


@bp.route('/', methods=['GET'])
def index():
    # login info
    login_info = get_login_info()
    return create_template('index.html', title='', login_info=login_info)


@bp.route('/login', methods=['POST'])
def login():
    if get_login_info():
        flash('すでにログインしています')
        return redirect('/')

    user_id = request.form.get('user_id')
    if user_id:
        session_login(user_id)
    else:
        # エラーメッセージの登録
        flash('なにか名前を入力してください')

    app.logger.debug(f'login {user_id}')
    return redirect('/')


@bp.route('/logout', methods=['GET'])
@check_login
def logout():
    session_logout()
    return redirect('/')
