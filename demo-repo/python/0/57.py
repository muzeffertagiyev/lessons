def username(name,surname):
    return name+" "+surname


def userinfo(name,surname,age="35"):
    userfio=username(name,surname)
    return f"{userfio} is {age} years old"


print(userinfo("Mizi","Veliyev"))
