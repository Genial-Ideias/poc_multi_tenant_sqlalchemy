from dependency_injector import containers, providers

from src.domain.users.repositories.user_repository import UserRepository



class UserContainer(containers.DeclarativeContainer):

    tenant_db = providers.Dependency()

    user_repository = providers.Factory(
        UserRepository,
        session_factory=tenant_db.provided.session,
    )
