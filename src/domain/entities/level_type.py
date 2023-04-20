from dataclasses import dataclass
from src.domain.entities.bases.described_class_base import DescribedClassBase

@dataclass
class LevelType (DescribedClassBase):
    _class_name= 'nível'
    _gender_name= 'do'
