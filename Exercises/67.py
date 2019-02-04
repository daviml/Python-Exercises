x = s = 0
while True:   
    x = int(input('Digite um numero: ')) 
    if x < 0:
        break
    for j in range(1,11):        
        print(f'{x} X {j} = {x*j}')