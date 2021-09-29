hm_ticket=int(input('Введите количество билетов которые которые желаете приобрести:'))
list_of_age=[input(f'Введите возраст посетителя с билетом {i+1}:')for i in range(hm_ticket)]
#обявляем стоимость билетов
price_1=0
price_2=990
price_3=1390
#обьявляем списки возрастов
age_1=[i for i in range(18)]
age_2=[i for i in range(18,25)]
age_3=[i for i in range(25,100)]
for i in range(len(list_of_age)):
    if int(list_of_age[i]) in age_1:
          price_1+=price_1
    if int(list_of_age[i]) in age_2:
          price_1+=price_2
    if int(list_of_age[i]) in age_3:
          price_1+=price_3
#расчет скидки 10% если куплено более 3 билетов
if len(list_of_age)>3:
    print("Общаяя стоимость, с учетом скидки 10%:", price_1*(0.9),"рублей")
else:
    print("Общаяя стоимость:", price_1, "рублей")
