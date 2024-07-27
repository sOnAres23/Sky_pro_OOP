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
