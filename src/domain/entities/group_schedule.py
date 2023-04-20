from dataclasses import dataclass
from src.domain.entities.bases.class_base import ClassBase

@dataclass
class GroupSchedule(ClassBase):
    _class_name= 'Turma'
    _gender_name= 'da'

    def validate(self) -> None:
        super().validate()

