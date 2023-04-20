from dataclasses import dataclass
from src.infra.repositories.implementation.base.described_repository import DescribedRepository
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.domain.entities import LevelType

@dataclass
class LevelTypeRepository (DescribedRepository):
    def __init__(self, db: IDbHandler):
        super().__init__(db, LevelType)
