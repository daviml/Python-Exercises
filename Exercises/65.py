cont = 0
som = 0
med = 0
q = 0
c = int(input('digite um numero: '))
q = int(input('quer digitar mais? 1 para sim 2 para nao'))
ma = c
me = c
if q == 2:
    cont = 1
    som = c
while q != 2:
    c = int(input('digite um numero: '))
    q = int(input('quer digitar mais? 1 para sim 2 para nao'))
    
    som = som + c
    if cont == 0:
        ma = me = c
    else:
        if c > ma:
            ma = q
        if c < me:
            me = c
    cont += 1
med = som/cont
print('med= {} ... maior= {} ... menor= {}'.format(med,ma,me))