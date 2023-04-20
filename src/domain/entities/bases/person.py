from dataclasses import dataclass
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.validators.domain_validator import DomainValidator
from src.domain.entities.bases.class_base import ClassBase
from src.domain.config.config_atributes import EMAIL_FIELD, NAME_FIELD, CELLPHONE_FIELD


@dataclass
class Person(ClassBase):
    _class_name= 'Classe Base Pessoa'
    _gender_name= 'da'
    cpf: str = ''
    email: str = ''
    name: str = ''
    cell_phone: str = ''
    cell_phone2: str = ''

    def validate(self):
        super().validate()
        DomainValidator.validate_email(self.email, f'email {self._repr}',min_len=EMAIL_FIELD.min, max_len=EMAIL_FIELD.max)
        DomainValidator.string_required(self.name, f'nome {self._repr}', exact_len=NAME_FIELD.exact, min_len=NAME_FIELD.min, max_len=NAME_FIELD.max)
        DomainValidator.validate_cell_phone(self.cell_phone, f'Celular {self._repr}', CELLPHONE_FIELD.exact)
        if (self.cell_phone2):
            if (self.cell_phone == self.cell_phone2):
                raise DomainValidationError(f'Segundo Celular {self._repr} não pode ser o mesmo que o primeiro')    
            DomainValidator.validate_cell_phone(self.cell_phone2, f'Segundo Celular {self._repr}', CELLPHONE_FIELD.exact)
  