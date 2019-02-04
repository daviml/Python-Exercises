ma = 0
me = 0
for c in range(0,5):
    p = int(input('digite seu peso: '))
    if c == 0:
        ma = p
        me = p
    else:        
        if p > ma:
            ma = p
        if p < me:
            me = p
print('maior {}'.format(ma))
print('menor {}'.format(me))