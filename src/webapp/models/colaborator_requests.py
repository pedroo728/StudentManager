from dataclasses import dataclass
from typing import Optional

@dataclass
class ColaboratorRequestUpdate:
    email: str = ''
    name: str = ''
    cell_phone: str = ''
    cell_phone2: Optional[str] = None
    colaborator_type_id: int = 0

@dataclass
class ColaboratorRequestInsert (ColaboratorRequestUpdate):
    cpf: str = ''
