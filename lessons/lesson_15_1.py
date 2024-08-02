# class Employee:
#     """Класс для представления сотрудника"""
#     name: str
#     surname: str
#     email: str
#     pay: int
#
#     def __init__(self, name, surname, pay):
#         self.__name = name
#         self.__surname = surname
#         self.pay = pay
#         self._email = f'{name}_{surname}@gmail.com'
#
#     def __str__(self):
#         return f'{self.__name} {self.__surname} ({self.pay})'
#
#     def __repr__(self):  # метод для разработчиков
#         return f'{self.__class__.__name__} ("{self.__name}", "{self.__surname}", {self.pay})'
#
#     def __add__(self, other):
#         """
#         Метод срабатывает, когда используется оператор сложения.
#         В параметре other хранится то, что справа от знака +
#         """
#         return self.pay + other.pay
#
#     def __len__(self):
#         return len(f'{self.__name} {self.__surname}')
#
#
# emp_1 = Employee('Ivan', 'Ivanov', 50000)
# emp_2 = Employee('Petr', 'Petrov', 60000)
#
# s_emp = str(emp_1)
#
# print(type(s_emp))
# print(s_emp)
#
# print(repr(emp_1))  # метод для разработчиков
#
# print(emp_1 + emp_2)
#
# print(len(emp_1))
