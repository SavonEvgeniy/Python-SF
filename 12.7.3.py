per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита:"))
per_cent_values = list(per_cent.values()) #формируем список значений из per_cent
profit = [round((i*money)/100,2) for i in per_cent_values] #генератор списка
max_profit = max(profit) #поиск максимального значения
print(profit)
print("Максимальная сумма, которую вы можете заработать-", round(max_profit,2))

