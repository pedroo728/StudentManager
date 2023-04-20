from dataclasses import dataclass
from typing import Any
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.infra.repositories.implementation.base.repository_base import RepositoryBase
from src.domain.entities.bases.class_base import ClassBase
from src.domain.enums.status_enum import StatusEnum

@dataclass
class RepositoryCRUD (RepositoryBase):
    def __init__(self, db: IDbHandler, entity: Any):
        super().__init__(db, entity)

    def add(self, obj: ClassBase) -> None:
        obj.id = None
        obj.status = StatusEnum.ATIVO
        self._session.add(obj)
        self._session.flush()

    def delete(self, obj: ClassBase) -> None:
        obj.status = StatusEnum.LOGICAMENTE_DELETADO
