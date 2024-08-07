# class StripChars:
#     """Класс, удаляющий определенные символы из строки"""
#     def __init__(self, chars):
#         """Инициализация символов для удаления"""
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         """Удаление символов из строки"""
#         return args[0].strip(self.__chars)
#
#
# st1 = StripChars('?')
# st2 = StripChars('!')
#
# res = st1('?Example?')
# rese = st2('!SomeExample!')
#
# print(res)
# print(rese)
#
#
# class EvenRange:
#     """Класс-Итератор, возвращающий только четные числа в диапазоне от 0 до stop"""
#     def __init__(self, stop):
#         self.stop = stop
#
#     def __iter__(self):
#         """Возвращает итератор"""
#         self.current_value = -2
#         return self
#
#     def __next__(self):
#         """Возвращает следующее четное число в диапазоне"""
#         if self.current_value + 2 < self.stop:
#             self.current_value += 2
#             return self.current_value
#         else:
#             raise StopIteration
#
#
# for i in EvenRange(7):
#     print(i)
#
#
# class MyOpen:
#     def __init__(self, filename, mode='r'):
#         """
#         Класс, который создает объект, который можно использовать
#         вместо open(), чтобы автоматически закрывать файл.
#         :param filename: имя файла
#         :param mode: режим открытия файла (по умолчанию 'r')
#         """
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         """
#         Метод, который вызывается при входе в блок контекста.
#         Он открывает файл и возвращает файловый дескриптор.
#         :return: файловый дескриптор
#         """
#         self.fp = open(self.filename, self.mode)
#         return self.fp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """
#         Метод, который вызывается при выходе из блока контекста.
#         Он закрывает файл.
#         """
#         self.fp.close()
#
#
# with MyOpen('example.txt', 'r') as fp:  # Открываем файл
#     print(fp.read())  # Читаем файл
