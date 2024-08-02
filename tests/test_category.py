from src.category import Category


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3

    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который "
                                           "позволяет наслаждаться просмотром, станет вашим другом и помощником")
    assert len(second_category.products) == 1

    assert Category.product_count == 4
    assert Category.category_count == 2


def test_get_product_list_property(first_category):
    assert (
            first_category.get_products_list
            == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
               "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
               "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_str(first_category):
    assert str(first_category) == 'Смартфоны, количество продуктов: 27 шт.'


# def test_product_iterator(product_iterator):
#     assert product_iterator.index == 0
