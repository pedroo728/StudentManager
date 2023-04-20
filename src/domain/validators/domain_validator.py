import re
from src.domain.exceptions.domain_validation_error import DomainValidationError

class DomainValidator:
    @staticmethod
    def string_required(value: str, field_name: str, exact_len: int = 0, min_len: int = 0, max_len: int = 0) -> None:
        DomainValidationError.when(isinstance(value, str) is False, f"{field_name} não é uma string")
        DomainValidationError.when(value is None, f'{field_name} está vazio')

        value = value.strip()

        DomainValidationError.when(len(value) == 0, f'{field_name} não pode ser vazio')
        if (exact_len > 0):
            DomainValidationError.when(len(value) != exact_len, f'{field_name} deve ter tamanho de {exact_len}')
        else:
            DomainValidationError.when(min_len > 0 and len(value) < min_len, f'{field_name} deve ter tamanho minimo de {min_len}')
            DomainValidationError.when(max_len > 0 and len(value) > max_len, f'{field_name} deve ter tamanho máximo de {max_len}')

    @classmethod
    def validate_email(cls, value: str, field_name: str, min_len: int = 0, max_len: int = 0) -> None:
        cls.string_required(value, field_name, 0, min_len, max_len)
        value = value.strip()
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        DomainValidationError.when(re.fullmatch(regex, value) is None, f'{field_name} não é um email')

    @classmethod
    def validate_cell_phone(cls, value: str, field_name: str, exact_len: int = 0) -> None:
        cls.string_required(value, field_name, exact_len, 0, 0)
        value = value.strip()

        regex = re.compile(r'([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})')
        DomainValidationError.when(re.fullmatch(regex, value) is False, f'{field_name} não é um telefone celular')

    @staticmethod
    def validate_id(value: int, field_name: str) -> None:
        DomainValidationError.when(isinstance(value, int) is False, f"{field_name} não é um inteiro")
        DomainValidationError.when(value <= 0, f'{field_name} deve ser um inteiro positivo. [Id={value}]')
