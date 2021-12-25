# list verilir sene eger listdeki element cut ededdise o zaman hemin 
# elementi 3 e vurub print elemek tek ededdirse 2 ye vurub print elemek

digits=[5,7,8,10,22,12,15,13,21,24,30,31]

for digit in digits:
    if digit%2==0:
        print(digit*3)
    else:
        print(digit*2)        
        