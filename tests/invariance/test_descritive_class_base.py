import pytest
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.entities.bases.described_class_base import DescribedClassBase
from src.domain.enums.status_enum import StatusEnum


str_repr = 'do DescribedClassBase'

test_error_data = [
    (1, StatusEnum.ATIVO, None, f'Descrição {str_repr} não é uma string'),
    (1, StatusEnum.ATIVO, 10, f'Descrição {str_repr} não é uma string'),
    (1, StatusEnum.ATIVO, '1', f'Descrição {str_repr} deve ter tamanho minimo de 5'),
    (1, StatusEnum.ATIVO, 'x'*101, f'Descrição {str_repr} deve ter tamanho máximo de 100'),
]

@pytest.mark.parametrize("id, status, description, msg_expected", test_error_data)
def test_invalid_data_error(id, status, description, msg_expected):
    obj = DescribedClassBase(id=id, status=status, description=description)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == msg_expected
