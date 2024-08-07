# class Employee:
#     """Класс для представления сотрудника"""
#     name: str
#     surname: str
#     email: str
#     pay: int
#
#     raise_amount = 1.04  # Атрибут класса
#     # Переменная на уровне класса для подсчета количества сотрудников
#     number_of_employees = 0
#
#     def __init__(self, name, surname, pay):
#         """Метод для инициализации экземпляра класса"""
#         """Задаем значения атрибутам экземпляра"""
#         self.__name = name
#         self.__surname = surname
#         self.pay = pay
#         self._email = f'{name}_{surname}@gmail.com'
#         self.is_working = False
#         self.is_on_vacation = False
#
#         Employee.number_of_employees += 1
#
#     def fullname(self):  # Метод
#         """Метод, который возвращает полное имя сотрудника."""
#         return f'{self.__name} {self.__surname}'  # self использует данные конкретного экземпляра
#
#     def apply_raise(self):  # И это метод
#         pay_up = self.pay * self.raise_amount
#         return pay_up
#
#     def work(self):
#         self.is_working = True
#         self.is_on_vacation = False
#         print('Do some work')
#
#     def go_to_vacation(self):
#         self.is_working = False
#         self.is_on_vacation = True
#         print('Go to vacation')
#
#
# # Создаем 1-й экземпляр и передаем параметры для инициализации
# emp_1 = Employee('Ivan', 'Ivanov', 50000)
# # Создаем 2-й экземпляр и передаем параметры для инициализации
# emp_2 = Employee('Petr', 'Petrov', 60000)
#
# # Вызываем метод fullname экземпляра
# print(emp_1.fullname())
#
# print(emp_1.pay)
# print(emp_1.apply_raise())
# print(emp_1._email)
#
# # Вызываем метод fullname экземпляра
# print(emp_2.fullname())
#
# print(emp_2.pay)
# print(emp_2.apply_raise())
# print(emp_2._email)
#
# print(Employee.number_of_employees)
