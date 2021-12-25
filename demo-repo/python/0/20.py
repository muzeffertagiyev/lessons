# listde olan elementlerin sayi 5den az olarsa o 
# zaman bu listde userin daxil eeldiyi sozun sayini 
# hesablasin yox eger listde olan elementlerin sayi 5 ile 10 arasinda 
# olarsa onda userin daxil elediyi sozun indexini tapsin 10dan cox olarsa bu zaman 
# ekrana list cox uzundu sozunu cixarsin


user=input("Enter a word: ")
names=["ferid","muzeffer","perviz","ferid","ferid","ferid"]

if len(names)<5:
    print(names.count(user))
elif 5<len(names)<10:
    print(names.index(user))
else:
    print("list cox uzundu")



