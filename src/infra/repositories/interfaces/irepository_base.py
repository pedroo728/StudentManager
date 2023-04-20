from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from src.domain.entities.bases.class_base import ClassBase

@dataclass
class IRepositoryBase (ABC):

    @abstractmethod
    def get(self, id: int) -> ClassBase:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self) -> List[ClassBase]:
        raise NotImplementedError()

    @abstractmethod
    def exists(self, id: int, only_active: bool = False) -> bool:
        raise NotImplementedError()
