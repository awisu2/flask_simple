# import os
from glob import glob
from os.path import join, relpath, splitext, sep
from os import getcwd
from importlib import import_module

def add_blueprint_underdir(app, dir):
  """
  指定ディレクトリ配下のスクリプトを検索し、blueprintの取得とappへの登録を行う
  """
  pathes = glob(join(dir, '**', '*.py'), recursive=True)
  current_dir = getcwd()
  for path in pathes:
    # スクリプトパスから、import用の相対パスを生成
    name, _ = splitext(relpath(path, start=current_dir))
    name = name.replace(sep, '.')
    app.logger.debug(f'regist blueprint from {name}')

    # blueprintに登録
    module = import_module(name)
    app.register_blueprint(module.bp)


