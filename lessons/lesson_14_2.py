# from datetime import datetime
#
#
# class Employee:
#
#     num_of_emps = 0
#     raise_amt = 1.04
#
#     def __init__(self, name, surname, pay):
#         self.name = name
#         self.surname = surname
#         # self._email = f'{name}_{surname}@gmail.com'
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#     @classmethod
#     def set_raise_amt(cls, new_raise_amt):
#         cls.raise_amt = new_raise_amt
#
#     @staticmethod
#     def is_workday(date):
#         if date.weekday() == 5 or date.weekday() == 6:
#             return True
#
#         return False
#
#     @property  # Это свойство КЛАССА
#     def email(self):
#         return f'{self.name}_{self.surname}@gmail.com'
#
#     @property  # Это свойство КЛАССА
#     def fullname(self):
#         """Метод, который возвращает полное имя сотрудника."""
#         return f'{self.name} {self.surname}'
#
#     @fullname.setter
#     def fullname(self, new_fl):  # Метод
#         name, surname = new_fl.split(' ')
#         self.name = name
#         self.surname = surname
#
#
# emp_1 = Employee('Jon', 'Snow', 50000)
# emp_2 = Employee('Ivan', 'Ivanov', 60000)
#
# print(emp_1.fullname)
# print(emp_1.email)
#
# emp_1.fullname = 'Bob Sanders'
# print(emp_1.fullname)
#
# print(Employee.raise_amt)
#
# Employee.set_raise_amt(1.05)
#
# print(emp_1.raise_amt)
# # print(emp_2.raise_amt)
#
# emp_str_1 = 'Jon-Snow-70000'
# # emp_str_2 = 'Ivan-Ivanov-30000'
# # emp_str_3 = 'Elena-Nikitina-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.pay)
#
# my_date = datetime.now()
# print(Employee.is_workday(my_date))
