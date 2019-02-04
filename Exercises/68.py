from random import randint
v = 0 
while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Digite P para par ou I para impar: ')).upper()
    jogador = int(input('Digite seu valor entre 1 a 10 incluindo os mesmos: '))
    pc = randint(1,10)
    total = jogador + pc
    print(f'voce jogou {jogador} e o pc {pc}, a soma é {total}')
    
    if escolha == 'P':
        if total % 2 == 0:
            v += 1
            print('voce venceu')
        else:
            print('voce perdeu')
            break
    elif escolha == 'I':
        if total % 2 != 0:
            v += 1
            print('voce venceu')
        else:
            print('voce perdeu')
            break
    print('vamos jogar de novo...')
print(f'GAME OVER voce venceu {v} vezes')
    
