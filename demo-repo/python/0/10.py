word=input("Enter words: ")

names=["ferid","yusif","muzeffer","nicat","perviz","test","test","test"]

if len(names)>6:
    if names.count(word)>2:
        print(names.count(word)*3)
    else:
        print("2 den azdir")
else:
    print("say azdir")
