print("======================================================================================")
print("                                 PASSWORD CHECKER                                     ")
print("======================================================================================")


password="kaif alvi"


for i in range(1,4):
    given=input('give you password \n:')
    if password==given:
        print("correct password")
        break
    else:
        print("wrong")