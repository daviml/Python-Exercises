x = int(input('digite o primeiro valor: '))
y = int(input('digite o segundo valor: '))
op = 0
while op != 5:
    print('o que deseja fazer:')
    print('[1] somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novos numeros')
    print('[5]sair')
    op = int(input('opcao: '))
    if op == 1:
        print('soma = {}'.format(x+y))
    if op == 2:
        print('mult = {}'.format(x*y))
    if op == 3:
        if x > y:
            print(x)
        else:
            print(y)
    if op == 4:
        x = int(input('novo x: '))
        y = int(input('novo y: '))