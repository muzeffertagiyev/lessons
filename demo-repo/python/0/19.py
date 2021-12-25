#listde eger 4 varsa onda listin ilk 5 elementini cixarmaq yoxdursa onda listin birinci ve sonuncu reqemlerini cemi


digits=[3,6,7,5,8,7,9,4,10,11]

eded1=int(digits[0])
eded2=int(digits[-1])
cem=eded1+eded2
if 4 in digits:
    print(digits[0:5])
else:
    print(cem)    