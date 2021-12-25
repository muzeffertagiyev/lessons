# demeli bidene kitabxana sistemi qurmaq yeni kitabin adi
#  sayi yazilma tarixi sora bu kitabin kimlerde oldugu yeni 
# meselen ferid perviz muzeffer ve hemin adamlarin adlari soyadlari dogum tarixi


ferid={"name":"Ferid","surname":"Valiyev","age":23}
muzeffer={"name":"muzeffer","surname":"Tagiyev","age":22}
perviz={"name":"Perviz","surname":"Veliyev","age":21}


kitab={
    "name":"Agatha Christie",
    "number":"15",
    "date":"20.06.2020",
    "students":[
        ferid,
        muzeffer,
        perviz
    ]
}

for student in kitab["students"]:
    for key,value in student.items():
        print(key,value)



