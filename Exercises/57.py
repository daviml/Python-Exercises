c = 'a'
while c not in 'MmFf':
    c = str(input('digite um sexo [M/F]')).strip().upper()[0]
    print('tente novamente')
print('ok')
    