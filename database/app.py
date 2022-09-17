import click
from flask.cli import with_appcontext
from src.app.db import populate_db
from src.app import create_app, database
from src.app.routes import routes


app = create_app()
routes(app)


@click.command(name='populate_database')
@with_appcontext
def call_command():
    populate_db()


@click.command(name='drop_tables')
@with_appcontext
def drop_tables():
    database.drop_all()


app.cli.add_command(call_command)
app.cli.add_command(drop_tables)


if __name__ == "__main__":
    app.run()
