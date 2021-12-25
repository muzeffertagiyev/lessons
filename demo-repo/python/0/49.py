gamer1={"name":"Ronaldo","number":"7","age":"31"}
gamer2={"name":"Messi","number":"10","age":"30"}
gamer3={"name":"Ronaldinho","number":"15","age":"45"}
gamer4={"name":"Muller","number":"11","age":"34"}
gamer5={"name":"Neymar","number":"8","age":"26"}
gamer6={"name":"Salah","number":"22","age":"33"}
gamer7={"name":"Levandovski","number":"20","age":"27"}
gamer8={"name":"Samir","number":"4","age":"21"}
gamer9={"name":"Ferid","number":"31","age":"23"}
gamer10={"name":"Nicat","number":"13","age":"22"}
gamer11={"name":"Azer","number":"69","age":"24"}
gamer12={"name":"Orxan","number":"90","age":"37"}

team1={"gamers":[gamer1,gamer2,gamer3]}
team2={"gamers":[gamer4,gamer5,gamer6]}
team3={"gamers":[gamer7,gamer8,gamer9]}
team4={"gamers":[gamer10,gamer11,gamer12]}




for x in team3["gamers"]:
    print(x["name"])


#for x in team1["gamers"]:
    #for key,value in x.items():
        #print(key,value)