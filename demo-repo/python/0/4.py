ad=input("Please enter your full name: ")
age=input("Please enter your age: ")
education=input("Please enter your education level: ")
workplace=input("Please enter your work place: ")
job=input("Please enter your job: ")


message1="salam,{}.Yasin neqederdir? Menim yasim {}-dir.Tehsilin nedir? {} almisam.Harada ishleyirsen? {}-de ishleyirem {} kimi".format(ad,age,education,workplace,job)

#or

message2=f"salam,{ad}.Yasin neqederdir? Menim yasim {age}-dir.Tehsilin nedir? {education} almisam.Harada ishleyirsen? {workplace}-de ishleyirem {job} kimi."

print(message1)
print(message2)