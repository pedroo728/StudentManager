from datetime import datetime
import pytest
from src.domain.enums.status_enum import StatusEnum 
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.entities.group_student import GroupStudent

str_repr = 'do Aluno Turma'

test_group_id_data = [
    (None, None, None, f'Id {str_repr} não é um inteiro'),
    ('a', None, None, f'Id {str_repr} não é um inteiro'),
    (-1, None, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=-1]'),
    (0, None, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=0]'),
    (1, None, None, f'Id {str_repr} não é um inteiro'),
    (1, 'a', None, f'Id {str_repr} não é um inteiro'),
    (1, -1, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=-1]'),
    (1, 0, None, f'Id {str_repr} deve ser um inteiro positivo. [Id=0]'),
    (1, 1, None, f'Data {str_repr} não é uma data valida'),
    (1, 1, 'a', f'Data {str_repr} não é uma data valida'),
    (1, 1, 1, f'Data {str_repr} não é uma data valida')
]

@pytest.mark.parametrize('group_id, student_id, start_date, expected', test_group_id_data)
def test_invalid_data_error(group_id, student_id, start_date, expected):
    obj = GroupStudent(id=1, status=StatusEnum.ATIVO,group_id=group_id, student_id=student_id, start_date=start_date)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == expected
    
def test_group_student_ok():
    obj = GroupStudent(id=1, status=StatusEnum.ATIVO, group_id=1, student_id=1, start_date=datetime.now())
    obj.validate()
    assert True