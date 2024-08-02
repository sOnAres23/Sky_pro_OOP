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
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Метод для подсчета общей суммы всех продуктов в данном классе"""
        self.total = self.__price * self.quantity
        self.total += other.__price * other.quantity
        return self.total

    @classmethod
    def new_product(cls, new_product: dict):
        """Класс-метод, который принимает на вход параметры товара в словаре и возвращает созданный объект класса"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]

        return cls(name, description, price, quantity)

    @property  # Это свойство КЛАССА
    def price(self) -> object:
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > value:
                print(f'Вы действительно хотите понизить цену с {self.__price} до {value}? Выберите: "yes" или "no"')
                user_input = input()
                if user_input == 'yes':
                    self.__price = value
                else:
                    self.__price = self.__price
