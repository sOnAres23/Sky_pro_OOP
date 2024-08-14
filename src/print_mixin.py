class PrintMixin:
    """Класс для логирования, момента создания экземпляров класса"""
    def __init__(self):
        print(repr(self))
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
