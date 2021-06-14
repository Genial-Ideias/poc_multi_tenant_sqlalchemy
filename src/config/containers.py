from dependency_injector import containers, providers

from src.config.env import environment
from src.config.database import Database

from src.infra.containers.tenants import TenantContainer

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Singleton(
            Database, db_url=environment.get_item('DATABASE_URL') if not environment.get_item('TESTING', False) else environment.get_item('DATABASE_TEST_URL', 'sqlite:///')
        )

    tenant_container = providers.Container(TenantContainer, db=db)


def init_app() -> Container:
    return Container()
