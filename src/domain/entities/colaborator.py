from dataclasses import dataclass
from src.domain.validators.domain_validator import DomainValidator

from src.domain.entities.bases.person import Person

@dataclass
class Colaborator(Person):
    _class_name= 'Colaborador'
    _gender_name= 'do'
    colaborator_type_id: int = 0

    def validate(self)->None:
        super().validate()
        DomainValidator.validate_id(self.colaborator_type_id, f'Tipo {self._repr}')
