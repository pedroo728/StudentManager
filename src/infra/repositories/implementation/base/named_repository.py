from dataclasses import dataclass
from typing import Any
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.infra.repositories.implementation.base.repository_base import RepositoryBase
from src.domain.entities.bases.named_class_base import NamedClassBase
from src.domain.enums.status_enum import StatusEnum

@dataclass
class NamedRepository (RepositoryBase):
    def __init__(self, db: IDbHandler, entity: Any):
        super().__init__(db, entity)

    def get_by_name(self, name: str) -> NamedClassBase:
        query = self._session.query(self._entity).filter_by(name = name)
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()
