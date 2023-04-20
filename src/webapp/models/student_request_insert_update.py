from dataclasses import dataclass
from typing import Optional

@dataclass
class StudentRequestInsertUpdate:
    cpf: str
    email: str = ''
    name: str = ''
    cell_phone: str = ''
    cell_phone2: Optional[str] = None
    situation: int = 1
