from src.product import Product


def test_product_init_1(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_init_2(second_product):
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_new_product(product_dict):
    product5 = Product.new_product(product_dict)
    assert product5.name == "Samsung Galaxy S23 Ultra"
    assert product5.description == "128GB, Зелёный цвет, 200MP камера"
    assert product5.price == 140000.0
    assert product5.quantity == 8


def test_prod_price_property(capsys, first_product):
    first_product.price = -180000.0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    first_product.price = 180000.0
    assert first_product.price == 180000.0


def test_product_str(first_product, second_product):
    assert str(first_product) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert str(second_product) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'


def test_product_add(first_product, second_product):
    assert first_product + second_product == 2580000.0
