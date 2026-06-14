print("======================================================================================")
print("                               GENERAL calculator                                     ")
print("======================================================================================")


a=int(input("enter 1st number"))
b=int(input("input 2nd number"))
c=input("give operator(+,-,*,/,avg)")
if c== "+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="avg":
    print((a+b)/2)
else :
    print("it s invald.\nvalid is ➡️+,-,*,/,avg")