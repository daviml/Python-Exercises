count = 0
x = int(input('digite o numero: '))
for c in range(1,x+1):
    if x%c==0:
        count += 1
if count == 2:
    print('primo')
else:
    print('nao é primo')