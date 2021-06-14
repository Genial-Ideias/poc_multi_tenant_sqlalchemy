from typer import Typer

from src.infra.cli import tenants

def init_app(app: Typer):
    app.add_typer(tenants.app, name='tenants')
