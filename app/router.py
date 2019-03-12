# import os
from os.path import dirname, join
from .libs.router import add_blueprint_underdir

def init_router(app):
  """
  routerの初期化
  """
  app.logger.debug('init_router start')

  # 指定ディレクト配下をblueprintに登録
  dirs = app.config.get('ROUTER_DIRS')
  if dirs:
    base_dir = app.config.get('APP_DIR')
    for dir in dirs:
      add_blueprint_underdir(app, join(base_dir, dir))
