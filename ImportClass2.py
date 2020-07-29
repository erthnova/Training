import Car #импорт всего модуля, нужно указывать название перед классом
from Elecrocar import ElectroCar

a4 = Car.Car('audi', 'a4', 2016)
tesla = ElectroCar('tesla', 'S', 2018)

tesla.battery.description_battery()
print(a4.description_name())