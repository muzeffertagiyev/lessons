eded=45

i=0

while True:
    user_eded=int(input("Enter a number: "))
    i=i+1
    if user_eded>eded:
        print("bundan kicik eded daxil et")
    elif user_eded==eded:
        print(f"Siz duz tapdiz {i}-ci cehdde")
        break

    else:
        print("bundan boyuk eded daxil et")
          
        