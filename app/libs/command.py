from glob import glob
from os.path import join, relpath, splitext, sep
from os import getcwd
from importlib import import_module


def init_command(app):
    """
    custom commandの初期化
    """
    dirs = app.config.get('COMMAND_DIRS')
    if dirs:
        base_dir = app.config.get('APP_DIR')
        for dir in dirs:
            add_command_underdir(app, join(base_dir, dir))


def add_command_underdir(app, dir):
    """
    指定ディレクトリ配下のスクリプトを検索し、appgroupの取得とappへの登録を行う
    肝心なのは、`app.cli.add_command()`で登録すること
    """

    pathes = glob(join(dir, '**', '*.py'), recursive=True)
    current_dir = getcwd()
    for path in pathes:
        # スクリプトパスから、import用の相対パスを生成
        name, _ = splitext(relpath(path, start=current_dir))
        name = name.replace(sep, '.')
        app.logger.debug(f'regist command from {name}')

        # commandに登録
        module = import_module(name)
        app.cli.add_command(module.appgroup)
