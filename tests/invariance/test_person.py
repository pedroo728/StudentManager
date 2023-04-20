import pytest
from src.domain.config.config_atributes import NAME_FIELD, EMAIL_FIELD, CELLPHONE_FIELD
from src.domain.entities.bases.person import Person
from src.domain.enums.status_enum import StatusEnum
from src.domain.exceptions.domain_validation_error import DomainValidationError

email_maxlen = EMAIL_FIELD.max + 1
name_minlen = NAME_FIELD.min -1
name_maxlen = NAME_FIELD.max + 1
cellphone_len = CELLPHONE_FIELD.exact + 1
str_repr = 'da Classe Base Pessoa'

test_data = [
    (None, None, None, None, f'email {str_repr} não é uma string'),
    ('', None, None, None, f'email {str_repr} não pode ser vazio'),
    ('t'*email_maxlen, None,None, None, f'email {str_repr} deve ter tamanho máximo de 100'),
    ('1.@.com', None, None, None, f'email {str_repr} não é um email'),
    ('sergio@gmail.com', None, None, None, f'nome {str_repr} não é uma string'),
    ('sergio@gmail.com', '', None, None, f'nome {str_repr} não pode ser vazio'),
    ('sergio@gmail.com', 't'*name_minlen, None, None, f'nome {str_repr} deve ter tamanho minimo de 5'),
    ('sergio@gmail.com', 't'*name_maxlen, None, None, f'nome {str_repr} deve ter tamanho máximo de 100'),
    ('sergio@gmail.com', 'Sergio Wellington', None, None, f'Celular {str_repr} não é uma string'),
    ('sergio@gmail.com', 'Sergio Wellington', '1', None, f'Celular {str_repr} deve ter tamanho de 11'),
    ('sergio@gmail.com', 'Sergio Wellington', '1'*cellphone_len, None, f'Celular {str_repr} deve ter tamanho de 11'),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '1', f'Segundo Celular {str_repr} deve ter tamanho de 11'),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '1'*cellphone_len, f'Segundo Celular {str_repr} deve ter tamanho de 11'),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '21964049400', f'Segundo Celular {str_repr} não pode ser o mesmo que o primeiro'),
]

@pytest.mark.parametrize("email, name, cell_phone, cell_phone2, expected", test_data)
def test_invalid_data_error(email, name, cell_phone, cell_phone2, expected):
    obj = Person(id=1, status=StatusEnum.ATIVO, email=email, name=name, cell_phone=cell_phone, cell_phone2=cell_phone2)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == expected

def test_person_ok():
    obj = Person(id=1, status=StatusEnum.ATIVO, email='pedrof728@gmail.com', name='Pedro Rodrigues', cell_phone='21964049400', cell_phone2='21989593059')
    obj.validate()
    assert True