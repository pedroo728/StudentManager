from dataclasses import dataclass
from src.domain.validators.domain_validator import DomainValidator
from src.domain.entities.bases.class_base import ClassBase
from src.domain.config.config_atributes import DESCRIPTION_FIELD

@dataclass
class DescribedClassBase(ClassBase):
    _class_name= 'DescribedClassBase'
    _gender_name= 'do'
    description: str = ''

    def validate(self)->None:
        super().validate()
        DomainValidator.string_required(self.description, f'Descrição {self._gender_name} {self._class_name}', exact_len=DESCRIPTION_FIELD.exact, min_len=DESCRIPTION_FIELD.min, max_len=DESCRIPTION_FIELD.max)
