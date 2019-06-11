from flask import render_template, current_app as app


def create_template(templatename, *, title='', **args):
    """
    テンプレートの作成、共通で利用するパラメータをセット
    """
    _args = {
        'config': app.config,
        'title': title,
    }
    for k in args:
        _args[k] = args[k]

    return render_template(templatename, **_args)
