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

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def get_products_list(self):
        product_list = ""
        for product in self.__products:
            product_list += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return product_list
