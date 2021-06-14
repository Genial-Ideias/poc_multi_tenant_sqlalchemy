from typer import Typer

from src.infra.cli import tenants, users

def init_app(app: Typer):
    app.add_typer(tenants.app, name='tenants')
    app.add_typer(users.app, name='users')
