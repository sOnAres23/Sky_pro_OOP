from src.product import Product


class Category:
    """Класс для описания категорий продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        self.sum_product = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {self.sum_product} шт."

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property  # Это свойство КЛАССА
    def products(self):
        return self.__products

    @property
    def get_products_list(self) -> str:
        """Метод для получения информации о продуктах в классе Category"""
        product_list = ""
        for product in self.__products:
            product_list += f'{str(product)}\n'

        return product_list
