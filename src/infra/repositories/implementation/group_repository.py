from dataclasses import dataclass
from src.infra.repositories.implementation.base import RepositoryCRUD, RepositoryBase
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.domain.entities import Group

@dataclass
class GroupRepository (RepositoryCRUD, RepositoryBase):
    def __init__(self, db: IDbHandler):
        super().__init__(db, Group)
