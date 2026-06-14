print("======================================================================================")
print("                                TASK LISTING                                          ")
print("======================================================================================")
tasks=[]

while True:
    task=input("enter your task")
    if task=="exit":
        break
    tasks.append(task)

print(tasks)