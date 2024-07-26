class Product:
    """Класс для описания продукта"""
    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
