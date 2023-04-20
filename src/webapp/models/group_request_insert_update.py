from dataclasses import dataclass
from datetime import time
from typing import Optional

@dataclass
class GroupRequestInsertUpdate:
    group_id: int = 1
    colaborator_id: int = 1
    horario: time = None
    max_size: int = 4
    level: str = ''
