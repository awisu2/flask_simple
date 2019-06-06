from datetime import timedelta
from os import getenv
from os.path import dirname

class DefaultConfig:
  # flask's config
  TESTING = False # test mode flag
  PERMANENT_SESSION_LIFETIME = timedelta(days=31) # (default: timedelta(days=31))
  SERVER_NAME = None # use by url_for(), cookie session. 設定する場合は起動時のhost、portと同一にする必要あり
  SECRET_KEY = b'\xab_\xfcC\x18js\xec><\xdb\xc640uH' # session cookie's key. (ex: `python -c 'import os; print(os.urandom(16))'`)

  # APPのディレクトリ
  APP_DIR = dirname(__file__)

  # 自動でrouterに登録する対象のディレクトリ
  ROUTER_DIRS = ['controllers']

  # 自動でcommandに登録する対象のディレクトリ
  COMMAND_DIRS = ['commands']

  # アプリがPRODUCTIONであるかフラグ
  APP_PROD = getenv('APP_ENV') == 'prod'

  # template用パラメータ
  SITE_NAME = 'flask simple'

  # db setting
  SQLALCHEMY_DATABASE_URI='postgresql://postgres@db/postgres' # dialect+driver://username:password@host:port/database
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  MIGRADE = getenv('MIGRADE') == '1'

  # session(need set db instance to app.config[SESSION_SQLALCHEMY])
  SESSION_SQLALCHEMY_TABLE = 'session'
  SESSION_TYPE = 'sqlalchemy'

class DevConfig:
  pass

class ProdConfig:
  pass