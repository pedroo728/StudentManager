from dataclasses import dataclass
from typing import Any
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.infra.repositories.implementation.base.repository_base import RepositoryBase
from src.domain.entities.bases.described_class_base import DescribedClassBase
from src.domain.enums.status_enum import StatusEnum

@dataclass
class DescribedRepository (RepositoryBase):
    def __init__(self, db: IDbHandler, entity: Any):
        super().__init__(db, entity)

    def get_by_description(self, description: str) -> DescribedClassBase:
        query = self._session.query(self._entity).filter_by(description = description)
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()