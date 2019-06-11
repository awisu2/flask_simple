from flask import session, redirect
from functools import wraps

LOGIN_KEY = 'login_info'


def login(info):
    """
    ログイン状態にする
    セッションにログイン情報を登録
    """
    session[LOGIN_KEY] = info


def logout():
    """
    ログアウト
    セッションからログイン情報を削除
    """
    session.pop(LOGIN_KEY)


def get_login_info():
    """
    ログイン情報の取得
    """
    return session.get(LOGIN_KEY)


def check_login(f):
    """
    デコレータ,ログイン情報を確認し、ログインしていなかったらtopにリダイレクト
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        if not (LOGIN_KEY in session):
            return redirect('/')

        return f(*args, **kwargs)

    return decorator
