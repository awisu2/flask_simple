database
--------

```bash
pip install Flask-SQLAlchemy
```

*database.py*

```py
def init_db(app, db):
  db.init_app(app)
```

__init__.py

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database import init_db

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  init_db(app, db)

  return app
```

migrate
-------

### setup

これらの準備後 `flask db {command}` が実行できるようになる

```bash
pip install Flask-Migrate
```

*database.py*

```python
from flask_migrate import Migrate

def init_db(app, db):
  db.init_app(app)
  Migrate(app, db)
```

### command

- init: `flask db init`
  - create *migrations* directory in current path
  