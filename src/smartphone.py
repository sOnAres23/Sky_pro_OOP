from src.product import Product


class Smartphone(Product):
    efficiency: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод для инициализации экземпляра класса"""
        super().__init__(name, description, price, quantity)  # Расширение в ходе наследования
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        self.__price = price

    def __add__(self, other):
        """Метод для подсчета общей суммы всех продуктов в данном классе"""
        if type(other) is Smartphone:
            self.total = self.__price * self.quantity
            self.total += other.__price * other.quantity
            return self.total
        raise TypeError
