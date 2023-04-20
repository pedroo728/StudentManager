from dataclasses import dataclass
from src.domain.exceptions.domain_validation_error import DomainValidationError

from src.domain.entities.bases.person import Person
from src.domain.enums.situation_student_enum import SituationStudentEnum

@dataclass
class Student(Person):
    _class_name= 'Aluno'
    _gender_name= 'do'
    situation: SituationStudentEnum = SituationStudentEnum.ATIVO

    def validate(self)->None:
        super().validate()
        DomainValidationError.when(self.situation not in list(SituationStudentEnum), f'Situação {self._repr} inválida. [Situacao={self.situation}]')
