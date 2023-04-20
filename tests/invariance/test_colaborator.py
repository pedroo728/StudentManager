# create pytest for colaborator.py

import  pytest
from src.domain.config.config_atributes import NAME_FIELD, EMAIL_FIELD, CELLPHONE_FIELD
from src.domain.enums.status_enum import StatusEnum
from src.domain.entities.colaborator import  Colaborator
from src.domain.exceptions.domain_validation_error import  DomainValidationError

email_maxlen = EMAIL_FIELD.max + 1
name_minlen = NAME_FIELD.min -1
name_maxlen = NAME_FIELD.max + 1
cellphone_len = CELLPHONE_FIELD.exact + 1
str_repr = 'do Colaborador'

test_data = [
    (None, None, None, None, f'email {str_repr} não é uma string', 0),
    ('a', None, None, None, f'email {str_repr} não é um email', 0),
    ('', None, None, None, f'email {str_repr} não pode ser vazio', 0),
    ('1.@gmail.com', None, None, None, f'email {str_repr} não é um email', 0),
    ('sergio@gmail.com', None, None, None, f'nome {str_repr} não é uma string', 0),
    ('sergio@gmail.com', '', None, None, f'nome {str_repr} não pode ser vazio', 0),
    ('sergio@gmail.com', 't'*name_minlen, None, None, f'nome {str_repr} deve ter tamanho minimo de 5', 0),
    ('sergio@gmail.com', 't'*name_maxlen, None, None, f'nome {str_repr} deve ter tamanho máximo de 100', 0),
    ('sergio@gmail.com', 'Sergio Wellington', None, None, f'Celular {str_repr} não é uma string', 0),
    ('sergio@gmail.com', 'Sergio Wellington', '1', None, f'Celular {str_repr} deve ter tamanho de 11', 0),
    ('sergio@gmail.com', 'Sergio Wellington', '1'*cellphone_len, None, f'Celular {str_repr} deve ter tamanho de 11', 0),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '1', f'Segundo Celular {str_repr} deve ter tamanho de 11', 0),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '1'*cellphone_len, f'Segundo Celular {str_repr} deve ter tamanho de 11', 0),
    ('sergio@gmail.com', 'Sergio Wellington', '21964049400', '21964049400', f'Segundo Celular {str_repr} não pode ser o mesmo que o primeiro', 0),
]

@pytest.mark.parametrize("email, name, cell_phone, cell_phone2, expected, colaborator_type_id", test_data)
def test_invalid_data_error(email, name, cell_phone, cell_phone2, expected, colaborator_type_id):
    obj = Colaborator(id=1, status=StatusEnum.ATIVO, email=email, name=name, cell_phone=cell_phone, cell_phone2=cell_phone2, colaborator_type_id=colaborator_type_id)
    with pytest.raises(DomainValidationError) as error:
        obj.validate()
    assert str(error.value) == expected

def test_colaborator_ok():
    obj = Colaborator(id=1, status=StatusEnum.ATIVO, email='pedrof728@gmail.com', name='Pedro Rodrigues', cell_phone='21964049400', cell_phone2='21989593059', colaborator_type_id=1)
    obj.validate()
    assert True
