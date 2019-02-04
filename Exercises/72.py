num = ('um','dois','tres','quatro','cinco')


while True:
    x = int(input('digite um numero entre 1 e 5'))
    if 0 < x < 6:
        print(num[x-1])
        break
    else:
        print('tente novamente')