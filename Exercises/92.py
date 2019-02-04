from datetime import datetime
now = datetime.now()

ppl = {}

ppl['nome'] = str(input('nome: '))
x = int(input('ano de nascimento:')) 
ppl['ano'] = (now.year) - x
y = int(input('ctps: (0 se nao tiver) '))
if y != 0:
    ppl['ctps'] = y
    ppl['contratacao'] = int(input('ano de contratacao: '))
    ppl['salario'] = int(input('salario: '))
    ppl['aposentadoria'] = (ppl['ano']) + 35


print(ppl)
print()
for k,v in ppl.items():
    print()
    print(f'a chave {k} tem o valor {v}')
