count1=0
count2=0
from datetime import date
ano = date.today()
x = int(ano.year)
for c in range(0,7):
    y = int(input('digite o ano de nascimento: '))
    idade = x - y
    if idade >= 18:
        count1 += 1
    else:
        count2 += 1
print('maiores: {}'.format(count1))
print('menores: {}'.format(count2))