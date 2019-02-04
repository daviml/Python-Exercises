print('\nCADASTRO DE PESSOAS\n')
m18 = 0
qh = 0
mm20 = 0
while True:
    print('\n')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite a sexo [M/F]: ')).upper()
    print('\n')
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        qh += 1
    if sexo == 'F' and idade < 20:
        mm20 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]: ')).upper()
    if cont == 'N':
        break
print(f'FIM DO PROGRAMA')
print(f'Pessoas com mais de 18 anos: {m18}')
print(f'{qh} homens cadastrados')
print(f'{mm20} mulheres com menos de 20 anos')

