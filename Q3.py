import numpy.random as nr

B10 = "000000000000000000111000100000001"
boolean = False
c=0
max=0
for i in range(len(B10)):
    if not(boolean):
        if B10[i] == '1':
            boolean=True
    elif B10[i]=='0':
        c = c +1
    elif B10[i]=='1':
        if c > max:
            max = c
            c = 0
        else:
            c =0
print(max)




