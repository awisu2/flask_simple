from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .libs.config import init_config
from .router import init_router
from .database import init_db
from .libs.command import init_command

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    init_config(app, __name__)

    # remote debug setting
    if app.config.get('REMOTE_DEBUGGING'):
        import ptvsd
        ptvsd.enable_attach(address=(
            app.config.get('REMOTE_HOST'),
            app.config.get('REMOTE_PORT')
        ), redirect_output=app.config.get('REDIRECT_OUTPUT'))
        ptvsd.wait_for_attach()

    init_db(app, db)

    # migrateモードの場合不要な処理はおこなわない
    if app.config.get('MIGRADE'):
        return app

    init_router(app)
    init_command(app)

    # session用テーブルインスタンスをセット
    app.config['SESSION_SQLALCHEMY'] = db

    return app
