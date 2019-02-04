from random import randint
count = 0
x = randint(0,10)
y = 11
while y != x:
    y = int(input('digite um numero: '))
    count += 1
print('conseguiu em {} tentativas'.format(count))