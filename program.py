'''==========================================='''
t= int(input('test cases'))
for i in range(t):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    name=input('\nenter string: ')
    n=int(input('\nenter increment: '))
    for i in  name:
        b=a.index(i)
        b=b+n
        if b>26:
            c=b%26
            b=-1
            b=b+c
            print(a[b],end='')
        else:
            print(a[b],end='')
'''======================================================='''



