# from src.product import Product
# from src.category import Category
#
#
# class ProductIterator:
#     """Класс для итерации продуктов класса Category"""
#
#     def __init__(self, category_obj: object):
#         self.category = category_obj
#         self.index = 0
#
#     def __iter__(self) -> object:
#         self.index = 0
#         return self
#
#     def __next__(self) -> object:
#         if self.index < len(self.category.get_products_list):
#             product = self.category.get_products_list[self.index]
#             self.index += 1
#             return product
#         else:
#             raise StopIteration
#
#
# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
# iterator = ProductIterator(category1)
#
# for item in iterator:
#     print(item)
