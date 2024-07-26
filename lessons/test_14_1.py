import pytest

from lessons.lesson_14_1 import Employee


@pytest.fixture()
def employee_ivan():
    return Employee('Ivan', 'Ivanov', 50000)


def test_init(employee_ivan):
    assert employee_ivan.name == 'Ivan'
    assert employee_ivan.surname == 'Ivanov'
    assert employee_ivan.email == 'Ivan_Ivanov@gmail.com'
    assert employee_ivan.pay == 50000


def test_work(employee_ivan):
    employee_ivan.work()
    assert employee_ivan.is_working
    assert not employee_ivan.is_on_vacation


def test_vacation(employee_ivan):
    employee_ivan.go_to_vacation()
    assert not employee_ivan.is_working
    assert employee_ivan.is_on_vacation
