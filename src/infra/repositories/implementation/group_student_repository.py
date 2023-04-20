from dataclasses import dataclass
from sqlalchemy import and_
from src.domain.enums.status_enum import StatusEnum
from src.infra.repositories.implementation.base import RepositoryCRUD, RepositoryBase
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.domain.entities import GroupStudent

@dataclass
class GroupStudentRepository (RepositoryCRUD, RepositoryBase):
    def __init__(self, db: IDbHandler):
        super().__init__(db, GroupStudent)

    def get_by_key(self, group_id: int, student_id: int) -> GroupStudent:
        query = self._session.query(self._entity).filter_by(and_(group_id = group_id, student_id=student_id))
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()