import click
from flask.cli import AppGroup

appgroup = AppGroup('sample')


@appgroup.command('hello')
@click.argument('name')
def helloworld(name):
    print(f'hello world and {name}!')
