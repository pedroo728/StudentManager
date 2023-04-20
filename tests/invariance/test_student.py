import pytest
from src.domain.config.config_atributes import NAME_FIELD, EMAIL_FIELD, CELLPHONE_FIELD
from src.domain.entities.student import Student
from src.domain.enums.status_enum import StatusEnum
from src.domain.exceptions.domain_validation_error import DomainValidationError


test_data = [
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '21964049401', None, f'Situação do Aluno inválida. [Situacao=None]'),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '21964049401', 0, f'Situação do Aluno inválida. [Situacao=0]'),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '21964049401', -1, f'Situação do Aluno inválida. [Situacao=-1]'),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '21964049401', 3, f'Situação do Aluno inválida. [Situacao=3]'),
]

@pytest.mark.parametrize("email, name, cell_phone, cell_phone2, situation, expected", test_data)
def test_invalid_data_error(email, name, cell_phone, cell_phone2,situation, expected):
    obj = Student(id=1, status=StatusEnum.ATIVO, email=email, name=name, cell_phone=cell_phone, cell_phone2=cell_phone2, situation=situation)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == expected

def test_person_ok():
    obj = Student(id=1, status=StatusEnum.ATIVO, email='pedrof728@gmail.com', name='Pedro Rodrigues', cell_phone='21964049400', cell_phone2='21989593059', situation=1)
    obj.validate()
    assert True