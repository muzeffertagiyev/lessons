ferid={"name":"Ferid","surname":"Veliyev","age":"23","university":"BMU"}
muzeffer={"name":"Muzeffer","surname":"Tagiyev","age":"22","university":"ADNSU"}
perviz={"name":"Perviz","surname":"Veliyev","age":"21","university":"BMU"}

users={ "userler":[ferid,muzeffer,perviz ]}



def axtar(user):
    for value in users["userler"]:
        if value["name"]==user:
            return value

print(axtar("Muzeffer"))
