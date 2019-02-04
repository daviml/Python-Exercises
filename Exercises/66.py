x = s = cont = 0
while True:
    x = int(input('Digite um valor: '))
    if x == 999:
        break
    s += x
    cont += 1
print(f'a soma dos {cont} numeros é {s}')