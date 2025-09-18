task=input("enter you task of today : \n").split(", ")
don_task=[]
not_don_task=[]
for fankshing in task:
    print(f"\n {fankshing}\n ")
    finsh=input("are finsh that : \n ")
    if finsh == "yes":
        print("good job keep up ")
        don_task.append(fankshing)
    elif finsh=="no":
        print("try do that to day ")
        not_don_task.append(fankshing)
    else:
        print(f"i do't undrstand {finsh} but if you finsh your task so you doing good \nand if you do't you have do that today")
    print("------------------")
chose=input("you wanna to see you task you day : \n ")
if chose=="yes":
    print(f"you do't do today {not_don_task}")
    print(f"you finsh to day {don_task}")
