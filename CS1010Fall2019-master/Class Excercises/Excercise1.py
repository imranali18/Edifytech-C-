print('How many friends are invited?')
a=int(input())
print('How many chocolates are there in this packet?')
b=int(input())
if b<a:
    print('You are short of ',a-b, 'chocolates')
elif b%a==0:
    c=b/a
    print('Chocolates will be evenly distributed and each friend gets',c, 'chocolates' )
else:
    d=b%a
    print('Chocolates cannot be evenly distributed because you have a surplus of ', d, 'chocolates')
