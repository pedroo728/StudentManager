from dataclasses import dataclass
from src.domain.validators.domain_validator import DomainValidator
from src.domain.entities.bases.class_base import ClassBase
from src.domain.config.config_atributes import NAME_FIELD

@dataclass
class NamedClassBase(ClassBase):
    _class_name= 'NamedClassBase'
    _gender_name= 'do'
    name: str = ''

    def validate(self)->None:
        super().validate()
        DomainValidator.string_required(self.name, f'Nome {self._gender_name} {self._class_name}', exact_len=NAME_FIELD.exact, min_len=NAME_FIELD.min, max_len=NAME_FIELD.max)
