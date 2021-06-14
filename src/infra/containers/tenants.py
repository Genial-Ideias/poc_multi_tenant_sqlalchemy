from dependency_injector import containers, providers

from src.domain.tenants.repositories.tenant_repository import TenantRepository
from src.domain.tenants.services import (
    CreateTenantService,
    ListTenantService
)


class TenantContainer(containers.DeclarativeContainer):

    db = providers.Dependency()

    tenant_repository = providers.Factory(
        TenantRepository,
        session_factory=db.provided.session,
    )

    create_tenant_service = providers.Factory(
        CreateTenantService,
        repository=tenant_repository
    )

    list_tenant_service = providers.Factory(
        ListTenantService,
        repository=tenant_repository
    )
