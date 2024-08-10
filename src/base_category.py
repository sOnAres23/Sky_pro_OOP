from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """Абстрактный класс, для класса Категории"""
    pass

    @abstractmethod
    def __str__(self) -> str:
        pass
