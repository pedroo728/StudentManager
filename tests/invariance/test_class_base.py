import pytest
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.entities.bases.class_base import ClassBase
from src.domain.enums.status_enum import StatusEnum

str_repr = 'da Classe Base'

test_error_data = [
    (None, None, f'Id {str_repr} não é um inteiro'),
    (-1, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=-1]'),
    (0, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=0]'),
    (1, None, f'Status {str_repr} inválido. [Status=None]'),
    (1, 5, f'Status {str_repr} inválido. [Status=5]'),
]

@pytest.mark.parametrize("id, status, msg_expected", test_error_data)
def test_classbase_invalid_date_error(id, status, msg_expected):
    obj = ClassBase(id=id, status=status)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == msg_expected


def test_classbase_ok():
    obj = ClassBase(id=1, status=StatusEnum.ATIVO)
    obj.validate()
    assert True
