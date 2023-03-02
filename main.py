# Входные данные
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую Вы планируете положить под проценты: '))

# Заполняем список deposit. Считаем, что начисленные проценты округляются до целого
percent_list = list(per_cent.values())
deposit = []
for i in percent_list:
    deposit.append(round(i * money / 100))
# Вывод списка deposit
print('Суммы, которые Вы можете заработать в разных банках:')
print(', '.join(map(str, deposit)))

# Выводим максимальное значение из списка deposit
print('-' * 60)
print('Максимальная сумма, которую Вы можете заработать — %d' % max(deposit))
