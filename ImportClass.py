from Car import Car, ElectroCar #импортируем по классам отдельно, указывать имя файла при присвоении не нужно


audia4 = Car('audi', 'a4', 2016)
tesla = ElectroCar('tesla', 'S', 2018)

tesla.battery.description_battery()
print(audia4.description_name())
