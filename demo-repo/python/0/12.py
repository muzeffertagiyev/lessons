a=int(input("eded1: "))
b=int(input("eded2: "))
c=int(input("eded3: "))

cem12=a+b
cem13=a+c
cem23=b+c

if cem12>10 and cem13>10:
    if cem12%4==0 and cem23%4==0:
        print(a-b+c)
    elif  cem12%4==0:
        print(cem12)
    else:
        print(cem23)
else:
    print(a+b+c)           