from os import getenv

def init_config(app, app_name):
  targets = ['default']

  # FLASK_APPの__name__をセット
  app.config['APP_NAME'] = app_name

  app.config['APP_ENV'] = getenv('APP_ENV', '')
  if app.config['APP_ENV']:
    targets.append(app.config['APP_ENV'])

  for target in targets:
    object_name = '{}.config.{}Config'.format(app_name, target.capitalize())
    app.logger.debug(f'load config from {object_name}')
    app.config.from_object(object_name)
