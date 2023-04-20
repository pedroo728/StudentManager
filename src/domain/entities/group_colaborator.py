from dataclasses import dataclass
from datetime import date
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.entities.bases.class_base import ClassBase
from src.domain.validators.domain_validator import DomainValidator

@dataclass
class GroupColaborator(ClassBase):
    _class_name= 'Colaborador da Turma'
    _gender_name= 'do'

    group_id: int = 0
    colaborator_id: int = 0
    start_date: date = date.today()

    def validate(self) -> None:
        super().validate()
        DomainValidator.validate_id(self.group_id, 'Id da Turma do Colaborador')
        DomainValidator.validate_id(self.colaborator_id, f'Id {self._repr}')
        DomainValidationError.when(not isinstance(self.start_date, date), f'Data {self._repr} não é uma data valida')
