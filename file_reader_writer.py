print("======================================================================================")
print("                           FILE READER SND WRITER                                     ")
print("======================================================================================")
f=open("r","kaif alvi")

action=input("what do you want?\n")

if action=="read":
    print(f.read())
    f.close()
elif acton=="write":
    f.write(input("enter your text"))
    f.close()