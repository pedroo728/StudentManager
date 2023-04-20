from dataclasses import dataclass
from src.domain.validators.domain_validator import DomainValidator
from src.domain.exceptions.domain_validation_error import DomainValidationError

from src.domain.entities.bases.class_base import ClassBase

@dataclass
class Group(ClassBase):
    _class_name= 'Turma'
    _gender_name= 'da'

    group_id: int = 0
    colaborator_id: int = 0
    # level: int = 0
    # max_size: int = 4
    
    def validate(self) -> None:
        super().validate()
        DomainValidator.validate_id(self.group_id, f'Id {self._repr}')
        DomainValidator.validate_id(self.colaborator_id, f'Id do Colaborador {self._repr}')
        DomainValidationError.when(not isinstance(self.group_id, int), f'Id {self._repr} não é um inteiro')
        DomainValidationError.when(not isinstance(self.colaborator_id, int), f'Id do Colaborador {self._repr} não é um inteiro')
        
        # TEM MAIS COISAS A IMPLEMENTAR
        
        # Como que faco para os tests do Group ja puxar os tests do Colaborador?
        #   -e o Colaborador tem que estar ATIVO para ser adicionado a uma Turma.