class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """"Инициализируем атрибуты имя и возраст"""
        self.name = name
        self.age = age
        #print("Собака создана")

    def sit(self):
        """"Собака будет садиться по команде"""
        print(self.name.title() + ' сел')

    def jump(self):
        """"Собака прыгает по команде"""
        print(self.name.title() + ' прыгнул по команде')

    def gav(self):
        print('Гав - Гав')

my_dog = Dog('Topik', 4)
my_dog2 = Dog('Nick', 7)
poppy = Dog('Poppy', 2)
my_dog.jump()
my_dog2.sit()
poppy.gav()