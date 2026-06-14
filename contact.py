print("======================================================================================")
print("                                CONTACT NUMBER LIST                                   ")
print("======================================================================================")

contact={}
n=int(input("how many list do you want"))

for i in range(0,n,1):
    name=input("enter name:")
    number=int(input("enter number"))

    contact[name]=number

print(contact)