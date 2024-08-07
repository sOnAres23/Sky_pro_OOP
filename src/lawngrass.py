from src.product import Product


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Метод для инициализации экземпляра класса"""
        super().__init__(name, description, price, quantity)  # Расширение в ходе наследования
        self.country = country
        self.germination_period = germination_period
        self.color = color
        self.__price = price

    def __add__(self, other):
        """Метод для подсчета общей суммы всех продуктов в данном классе"""
        if type(other) is LawnGrass:
            self.total = self.__price * self.quantity
            self.total += other.__price * other.quantity
            return self.total
        raise TypeError
