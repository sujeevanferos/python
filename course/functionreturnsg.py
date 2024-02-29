def painter():
    return "I am painter"
print(painter())

print()
# checking the username and passwords are valid
u_name="Sujeevan"
u_key="sujeevan2003"
name=input("USERNAME: ")
paswd=input("PASSWORD: ")
def validate():
    if(u_name==name and u_key==paswd):
        return "LOGIN SUCCEEDED"
    else:
        return "INVALID USERNAME OR PASSWORD !!!"
a=validate()
print(a)