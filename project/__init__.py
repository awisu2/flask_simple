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
    init_db(app, db)

    # migrateモードの場合不要な処理はおこなわない
    if app.config.get('MIGRADE'):
        return app

    init_router(app)
    init_command(app)

    # session用テーブルインスタンスをセット
    app.config['SESSION_SQLALCHEMY'] = db

    return app
