# listde eger ferid varsa feridi silib oinun yerine perviz yazmaq 
# ve yaxud eger muzeffer varsa o zaman liste hemde nicat elave elemek


names=["perviz","muzeffer","ferid","nicat","imamaddin"]

for index in range(len(names)):
    if names[index]=="ferid":
        del names[index]
        names.append("Perviz")
    if names[index]=="muzeffer":
        names.append("elvin")
print(names)            

        