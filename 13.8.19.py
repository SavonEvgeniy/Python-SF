hm_ticket=int(input('Введите количество билетов которые которые желаете приобрести:'))
L=[input(f'Введите возраст посетителя с билетом {i+1}:')for i in range(hm_ticket)]
#обявляем стоимость билетов
price1=0
price2=990
price3=1390
#обьявляем списки возрастов
age1=[i for i in range(18)]
age2=[i for i in range(18,25)]
age3=[i for i in range(25,100)]
for i in range(len(L)):
    if int(L[i]) in age1:
          price1+=price1
    if int(L[i]) in age2:
          price1+=price2
    if int(L[i]) in age3:
          price1+=price3
#расчет скидки 10% если куплено более 3 билетов
if len(L)>3:
    print("Общаяя стоимость, с учетом скидки 10%:", price1*(0.9),"рублей")
else:
    print("Общаяя стоимость:", price1, "рублей")
