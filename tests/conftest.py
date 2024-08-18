import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone

from src.product_iterator import ProductIterator


@pytest.fixture
def first_product():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


@pytest.fixture
def second_product():
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8)


@pytest.fixture
def first_category():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, "
                                "но и получения дополнительных функций для удобства жизни",
                    products=[Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                              Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                              Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
                              ]
                    )


@pytest.fixture
def second_category():
    return Category(name="Телевизоры",
                    description="Современный телевизор, который "
                                "позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    products=[Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)])


@pytest.fixture
def product_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "128GB, Зелёный цвет, 200MP камера",
        "price": 140000.0,
        "quantity": 8,
    }


@pytest.fixture
def first_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def second_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2,
                      "15", 512, "Gray space")


@pytest.fixture
def first_lawngrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture
def second_lawngrass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                     "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def product_iterator(first_category):
    return ProductIterator(first_category)


@pytest.fixture
def category_without_products():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [])
