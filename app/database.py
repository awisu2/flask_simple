def init_db(app, db):
  db.init_app(app)

  # migrate setting
  if app.config.get('MIGRADE'):
    from flask_migrate import Migrate
    Migrate(app, db)