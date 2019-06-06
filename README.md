# flask_simple

flaskの勉強がてら、通常必要になりそうな部分までを実装

## run

`docker-compose up`

after you can access *http://localhost:5000*

## run by command

### setuup(for local, for editor)

```py
# on venv
python3 -m venv .venv
source venv/bin/activate

# install
pip install --upgrade pip
pip install -r requirements.txt
```

- `APP_ENV=dev flask run --host=0.0.0.0 --port=5000`
  - with debug: `FLASK_ENV=development APP_ENV=dev flask run --host=127.0.0.1 --port=5000`
- FLASK_ENV: flaskフレームワーク自体の動作環境
- APP_ENV: アプリ自体の動作環境 *app.config.{APP_ENV}Config* のConfigを読み込みます
  - 'prod': productionになり、app.config['APP_PROD']がTrueになります

## migration sample

- document: [Welcome to Flask\-Migrate’s documentation\! — Flask\-Migrate documentation](https://flask-migrate.readthedocs.io/en/latest/#command-reference)

```bash
# init (create migrations directory)
docker-compose exec -e MIGRADE=1 flask_simple flask db init

# generate migrate script from models
docker-compose exec -e MIGRADE=1 flask_simple flask db migrate

# upgrade
docker-compose exec -e MIGRADE=1 flask_simple flask db upgrade

# downgrade
docker-compose exec -e MIGRADE=1 flask_simple flask db downgrade

# create new revision
docker-compose exec -e MIGRADE=1 flask_simple flask db revision
docker-compose exec -e MIGRADE=1 flask_simple flask db revision --rev-id 201903081537_createuser
```

## tests

`docker-compose run flask_simple pip install -e . && pytest`

- *NOTE*: `pip install -e .`は初回だけで良いので、upしたインスタンスにexecで代用しても良い。

## command

以下はサンプルコマンド、実態は*app/commands*配下のスクリプト

- `docker-compose run flask_simple sample hello foobar`
  - sample: appgroup
  - hello: function name
  - foobar: arg

commandの詳細はこちら、[Command Line Interface — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/cli/#custom-commands)
