from random import randint
from operator import itemgetter

jog = {}

jog['jog1'] = randint(0,10)
jog['jog2'] = randint(0,10)
jog['jog3'] = randint(0,10)
jog['jog4'] = randint(0,10)

print(jog)

rank = sorted(jog.items(),key=itemgetter(1),reverse=True)

for i,v in rank:
    print(i,v)
