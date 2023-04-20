from dataclasses import dataclass
from src.domain.entities.bases.described_class_base import DescribedClassBase

@dataclass
class ColaboratorType (DescribedClassBase):
    _class_name= 'tipo de colaborador'
    _gender_name= 'do'
     