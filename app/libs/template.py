from flask import render_template

def create_template(templatename, app, *, title='', **args):
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