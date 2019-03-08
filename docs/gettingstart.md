install
-------

```
python3 -m venv venv
source venv/bin/activate

pip install Flask
```

helloworld
----------

*__main__.py*

```python
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

`python3 .`

after you can access http://localhost:5000/

run on flask command
--------------------

**__main__.py**

```python
from app import app

if __name__ == '__main__':
    app.run(debug=True)
```

*app/__init__.py*

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, App!"

@app.route('/byebye', methods=['GET'])
def byebye():
    return "Bye Bye, App!"
```

`FLASK_ENV=development flask run --host=0.0.0.0`

- FLASK_ENV=development: set flask's environment, it set config ENV.(default: production)

flaskのconfigパラメータである ENV, DEBUG は特殊かつ重要なパラメータで、環境変数による設定が推奨される

### other environments

- FLASK_DEBUG: debug mode setting (default: 0)
  - ex: FLASK_DEBUG=1
  - default value change to 1 if FLASK_ENV is development.
- FLASK_APP=hello.py : run other script (default: app)


run with config and application factory
---------------------------------------

*app/templates/bybye.html*

```html
byebye {{name}}
```

*app/__init__.py*

```py
from flask import Flask, Blueprint, render_template
from datetime import timedelta

def create_app():
  app = Flask(__name__)

  app.config.from_mapping(
    TESTING=False, # test mode flag
    SECRET_KEY=b'\xedlE\xddEF\x1as\xf4\xf1\xd4\xfd\x8f\xc4\xf13', # session cookie's key. (ex: `python -c 'import os; print(os.urandom(16))'`)
    PERMANENT_SESSION_LIFETIME=timedelta(days=31), # (default: timedelta(days=31))
    # SERVER_NAME='127.0.0.1:5000' # use by url_for(), cookie session. 設定する場合は起動時のhost、portと同一にする必要あり
  )

  @app.route('/')
  def index():
    return "Hello, App!"

  bp = Blueprint('byebye', __name__, url_prefix='/byebye')
  @bp.route('/', methods=['GET'])
  @bp.route('/<name>', methods=['GET'])
  def byebye(name='foobar'):
    app.logger.debug(f'bybye {name}')
    return render_template('byebye.html', name=name)

  app.register_blueprint(bp)

  return app
```

FLASK_ENV=development flask run --host=127.0.0.1 --port=5000

- !appは`from flask import current_app`で取得可能

app functions
-------------

- logger: `app.logger.debug('logger debug')`
- g: `app.g`
  - unique for each request
- teardown_appcontext: `app.teardown_appcontext(foo_bar)`
  - regist function it's call cleaning up after returning the response
- cli.add_command: `app.cli.add_command(hello_world)`
  - ``

flask functions
---------------

- render_template: `use template for rendering`
  - it's use templates folder

links
-----

- tutorial: [Tutorial — Flask 1\.1\.dev documentation](http://flask.pocoo.org/docs/dev/tutorial/)
- deploy: [Deployment Options — Flask 0\.12\.4 documentation](http://flask.pocoo.org/docs/0.12/deploying/#deployment)
