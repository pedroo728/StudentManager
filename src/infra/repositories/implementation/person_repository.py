from dataclasses import dataclass
from typing import Any
from src.domain.enums.status_enum import StatusEnum
from src.infra.repositories.implementation.base.named_repository import NamedRepository
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.domain.entities import Person

@dataclass
class PersonRepository (NamedRepository):
    def __init__(self, db: IDbHandler, entity: Any):
        super().__init__(db, entity)

    def get_by_email(self, email: str) -> Person:
        query = self._session.query(self._entity).filter_by(email = email)
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()

    def get_by_cpf(self, cpf: str) -> Person:
        query = self._session.query(self._entity).filter_by(cpf = cpf)
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()
