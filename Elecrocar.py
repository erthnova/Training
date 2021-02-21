from Car import Car
#проверка репозитория
class Battery():
    """"Простая модель аккамулятора для электромобиля"""

    def __init__(self, battery=200):
        self.battery = battery

    def description_battery(self):
        """"Выводит информацию о мощности батареи"""
        print("Этот автомобиль имеет батарею мощностью " + str(self.battery) + " кВт")


class ElectroCar(Car):
    """"Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """"Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year)
        #self.battery = 100
        self.battery = Battery()

    def sun_recharge(self):
        print("Электрокар не поддерживает зарядку от солнца")

    def description_name(self):
        """"Переопределение родительского метода"""
        desc = 'Электромобиль ' + str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

#new comment