from dataclasses import dataclass
from src.infra.repositories.implementation.person_repository import PersonRepository
from src.infra.repositories.implementation.base.repository_crud import RepositoryCRUD
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.domain.entities import Student

@dataclass
class StudentRepository (PersonRepository, RepositoryCRUD):
    def __init__(self, db: IDbHandler):
        super().__init__(db, Student)
