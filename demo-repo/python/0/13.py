eded=int(input("Please insert a number with two digits: "))

eded1=eded%10
eded2=eded//10

umumi=eded1+eded2
hasil=eded1*eded2

if umumi>10:
    if hasil%4==0:
        print(umumi)
    elif hasil%4 !=0 and hasil%2==0:
        print("cut ededdir")
    else:
        print("tek ededdir")
else:
    print("bu eded balacadir")


