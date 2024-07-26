#  Наследование
class Employee:
    """ Класс сотрудника, который обладает общими свойстваи и методами"""
    name: str  # Указание атрибутов, которые будут доступны для объекта
    surname: str

    def work(self):
        print('Do some work')

    def go_to_vacation(self):
        print('Go to vacation')


class Developer(Employee):
    """ Дочерний класс от класса работника, который принимает и переопределяет некоторые свойства """
    language: str
    level: str

    def work(self):
        print('Write code')

    def read_documentation(self):
        print('Read documentation')


#  Полиморфизм
class JavaDeveloper:
    """Класс для представления Java-разработчиков."""

    def __init__(self, name):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Java-разработчике."""
        print(f'I am {self.name} - Java developer.')

    def code(self):
        """Метод для программирования на языке Java."""
        print("class HelloWorld { public static void main(String[] args)...")


class PythonDeveloper:
    """Класс для представления Python-разработчиков."""

    def __init__(self, name):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Python-разработчике."""
        print(f'I am {self.name} - Python developer.')

    def code(self):
        """Метод для программирования на языке Python."""
        print("print('Hello, World!')")


# Создаем экземпляры разных классов
dev1 = JavaDeveloper('Ivan')
dev2 = PythonDeveloper('Petr')

# Но работаем с ними единым образом
for developer in (dev1, dev2):
    developer.info()  # Вызов метода info()
    developer.code()  # Вызов метода code()
    print()
