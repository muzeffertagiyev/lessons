

i=0
while True:
    username_add=input("Username elave et: ")
    pasword_add=input("Pasword elave et: ")
    i=i+1
    if i==4:
        print("Giris blok olundu")
        break
    elif username_add.replace(" ","")=="admin" and pasword_add.replace(" ","")=="123":
        print(f"Girish olundur {i}-cu cehdde")
        break
    else:
        print("Tekrar sinayin")
    