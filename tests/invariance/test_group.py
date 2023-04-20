import pytest
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.entities.group import Group
from src.domain.enums.status_enum import StatusEnum


str_repr = 'da Turma'

test_group_error_data = [
    (None, None, f'Id {str_repr} não é um inteiro'),
    ('a', None, f'Id {str_repr} não é um inteiro'),
    (-1, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=-1]'),
    (0, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=0]'),
    (1, None, f'Id do Colaborador {str_repr} não é um inteiro'),
    (1, 'a', f'Id do Colaborador {str_repr} não é um inteiro'),
    (1, -1, f'Id do Colaborador {str_repr} deve ser um inteiro positivo. [Id=-1]'),
    (1, 0, f'Id do Colaborador {str_repr} deve ser um inteiro positivo. [Id=0]'), 
]



@pytest.mark.parametrize("group_id, colaborator_id, expected", test_group_error_data)
def test_group_id_error(group_id, colaborator_id, expected):
    obj = Group(id=1, status=StatusEnum.ATIVO, group_id=group_id, colaborator_id=colaborator_id)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == expected


def test_group_ok():
    obj = Group(id=1, status=StatusEnum.ATIVO, group_id=1, colaborator_id=1)
    obj.validate()
    assert True
