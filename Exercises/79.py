n = []

while (len(n)) < 5:

    x = int(input('digite um numero: '))
    if x in n:
        print('esse ja tem,tente novamente')
    else:
        n.append(x)
print(n)