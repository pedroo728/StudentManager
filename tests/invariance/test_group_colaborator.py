from datetime import datetime
import pytest
from src.domain.enums.status_enum import StatusEnum 
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.entities.group_colaborator import GroupColaborator

test_group_id_data = [
    (None, None, None, "Id da Turma do Colaborador não é um inteiro"),
    ("a", None, None, "Id da Turma do Colaborador não é um inteiro"),
    (-1, None, None, "Id da Turma do Colaborador deve ser um inteiro positivo. [Id=-1]"),
    (0, None, None, "Id da Turma do Colaborador deve ser um inteiro positivo. [Id=0]"),
    (1, None, None, "Id do Colaborador da Turma não é um inteiro"),
    (1, "a", None, "Id do Colaborador da Turma não é um inteiro"),
    (1, -1, None, "Id do Colaborador da Turma deve ser um inteiro positivo. [Id=-1]"),
    (1, 0, None, "Id do Colaborador da Turma deve ser um inteiro positivo. [Id=0]"),
    (1, 1, None, "Data do Colaborador da Turma não é uma data valida"),
    (1, 1, "a", "Data do Colaborador da Turma não é uma data valida"),
    (1, 1, 1, "Data do Colaborador da Turma não é uma data valida")
]

@pytest.mark.parametrize("group_id, colaborator_id, start_date, expected", test_group_id_data)
def test_invalid_data_error(group_id, colaborator_id, start_date, expected):
    obj = GroupColaborator(id=1, status=StatusEnum.ATIVO,group_id=group_id, colaborator_id=colaborator_id, start_date=start_date)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == expected
    
def test_group_colaborator_ok():
    obj = GroupColaborator(id=1, status=StatusEnum.ATIVO, group_id=1, colaborator_id=1, start_date=datetime.now())
    obj.validate()
    assert True