print("======================================================================================")
print("                                      EXPENSE TACKER                                  ")
print("======================================================================================")

expense=[]

for i in range(0,10,1):
    expense.append(int(input("your cost")))

print("your total cost=",sum(expense))