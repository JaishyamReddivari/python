import random

cpu = random.randint(0, 2)

start = input("Type 'START' to start Rock, Paper, Scissors game!\n")
if start == "START":
    user = int(input("Type '0' for Rock.\n     '1' for Paper.\n     '2' for Scissors.\n"))
    if user == 0:
        if cpu == 0:
            print("CPU went Rock. Draw!")
        elif cpu == 1:
            print("CPU went Paper. You Lose!")
        elif cpu == 2:
            print("CPU went Sciccors. You Win!")
    elif user == 1:
        if cpu == 0:
            print("CPU went Rock. You Win!")
        elif cpu == 1:
            print("CPU went Paper. Draw!")
        elif cpu == 2:
            print("CPU went Sciccors. You Lose!")
    elif user == 2:
        if cpu == 0:
            print("CPU went Rock. You Lose!")
        elif cpu == 1:
            print("CPU went Paper. You Win!")
        elif cpu == 2:
            print("CPU went Sciccors. Draw!")
    else:
        print("Invalid input!")
else:
    print("Invalid input!")
