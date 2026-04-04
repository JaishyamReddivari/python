print("Welcome to Trasure Island! Your mission is to find the trasure")
start = input("Type 'START' to begin the trasure hunt.\n")

if start == "START":
    print("You have arrived at a cross-road.")
    left_or_right = input("Do you want to go left or right? \n Type 'left' or 'right': ")
    if left_or_right == "left":
        swim_or_wait = input("You arrived at a lake. Do you want to swim or wait for the boat? \n Type 'swim' or 'wait': ")
        if swim_or_wait == "wait":
            print("The boat has arrived. The boat will take you to the next destination!")
            which_door = input("You have arrived at three doors, Red door, Blue door and Yellow door. Which door would you like to open? \nType 'red' or 'blue' or 'yellow': ")
            if which_door == "yellow":
                print("You found the treasure! You Win!")
            else:
                print("There was a tiger behind the red door. GAME OVER!")
        else:
            print("You drowned! GAME OVER!")
    else:
        print("You fell into a valley.\nGAME OVER!")
