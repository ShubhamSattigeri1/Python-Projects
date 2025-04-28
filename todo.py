print("Here is your To-Do list...")

list1 = []

def rerun():
    while True:
        list = input("Enter Your To-Do's : ")
        if list.lower() == "done":
            break
        else:    
         list1.append(list)
    print("\nYour todo list...")
    for i, task in enumerate(list1, 1):
        print(f"{i}. {task}")

rerun()

print("\n Want to edit more :\n1.Delete Item\n2.Add new item")   

option = int(input("Enter 1 or 2 : "))

if option == 1:
    pop = int(input("Enter the index you want to remove.")) 
    list1.pop(pop)
    for i, task in enumerate(list1, 1):
        print(f"{i}. {task}")

else:
    rerun()    

