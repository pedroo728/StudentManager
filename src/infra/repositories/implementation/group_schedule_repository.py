from dataclasses import dataclass
from src.infra.repositories.implementation.base.described_repository import DescribedRepository
from src.infra.adapters.database.interface_db_handler import IDbHandler
from src.domain.entities import GroupSchedule

@dataclass
class GroupScheduleRepository (DescribedRepository):
    def __init__(self, db: IDbHandler):
        super().__init__(db, GroupSchedule)

# Conferir se esta correto! 