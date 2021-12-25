# list verilir sene eger listdeki element 4e bolunurse bu zaman hemin 
# listdeki element 20 den boyuk olarsa bu zaman hemin elementi 6ya vur 
# eger 3 e bolunurse bu zaman hemin element eger 10 dan boyuk olarsa cemini
#  3e vur print ele diger halda yeni ne 4e need 3e bolunursa bu zaman hemin elementin
#  ozunu print ele


digits=[5,7,28,10,22,12,15,13,21,24,30,31,24,29,6]

for digit in digits:
    if digit%4==0:
        if digit>20:
            print(digit*6)
    elif digit%3==0:
        if digit>10:
            print(digit*3)
    else:
        print(digit)        
                