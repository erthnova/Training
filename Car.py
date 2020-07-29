class Car():
    """"Класс по созданию автомобиля"""
    def __init__(self, make, model, year):
        """"Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def description_name(self):
        """"Возвращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        """"Выводим пробег авто"""
        print("Пробег этого авто: " + str(self.odometer_reading) + ' км.')
    def update_odometer(self, km):
        """"Добавляем значение на одометре"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Не жульничай!")
    def increment_odometr(self, km):
        """"Увеличиваем показания одометра приращением"""
        if km > 0:
            self.odometer_reading += km
        else:
            print("Не жульничай!")

