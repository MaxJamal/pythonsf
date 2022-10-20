
money_count = input('Введите сумму, которую хотите положить на вклад: ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
list_of_per = per_cent.values()

deposit = []
for i in list_of_per:
    profit = i * float(money_count) / 100
    deposit.append(profit)
max_profit = max(deposit)
print('Максимальная сумма, которую вы можете заработать —', max_profit)

