per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита:"))
per_cent_values = list(per_cent.values())
profit = [(i*money)/100 for i in per_cent_values]
max_profit = max(profit)
print(profit)
print("Максимальная сумма, которую вы можете заработать -", int(max_profit))

