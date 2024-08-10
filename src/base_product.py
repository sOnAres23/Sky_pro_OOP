from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, для класса Продуктов"""
    pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
