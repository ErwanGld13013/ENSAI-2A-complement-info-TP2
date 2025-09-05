import copy

from business_object.statistic import Statistic
from abc import ABC, abstractmethod

class AbstractAttack(ABC):
    def __init__(self, power=None, name=None, descrption=None):
        self._power: int = power
        self._name: str = name
        self._description: str = description

    @abstractmethod
    def compute_damage(self) -> int:
