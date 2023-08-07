name = input("Type your name: ")
print("Welcome", name, "to your adventure!")
import random

optionz = ["rock", "paper", "scissors"]

answer = input("You're exploring a dungeon, you come to a split end with two pathways. Do you go left or right? ")

if answer == "left":
    #subcode
    answer = input("The path you chose takes you down a hallway with a suspicious button at the end. Will you press it? ")

    if answer == "yes":
        print("The button triggered a trap which shot you with blow darts. You died. ")
    elif answer == "no":
         print("You choose to return back to where you came from but stepped on a pressure plate you missed and ended up dying to a spike trap. ")
    else:
         print("Invalid choice. Game over. ") 

elif answer == "right":
    #subcode
    answer = input("The path you chose takes you to an open cave with two chests in the middle. Will you open the left or right chest? ")

    if answer == "left":
        answer = input("You find a key with a red jewel in it. After proceeding through the cave you find a gate with a similar jewel imbedded at the top  of it and a key slot. Do you want to insert the key and continue or return? (continue/return) ")
        if answer == "continue":
            answer = input("You open the gate and find yourself in a room with several statues and a man dressed as a mage at the end of it. He calls out to you and offers one of two spellbooks to pick from but to proceed you must win in a game of rock, paper, scissors or else he will take your life. (red book/blue book) ")
            while True:
                user_input = input("Choose one Rock/Paper/Scissors or flee to leave: ").lower()
                if user_input == "flee": 
                    print("You tried to leave, angering the Mage resulting in your death.")
                    quit()
    
                if user_input not in optionz:
                    continue

                random_number = random.randint(0, 2)
                # (rock = 0) (paper = 1) (scissors = 2)
                computer_pick = optionz[random_number]
                print("Mage picked,", computer_pick + ".")

                if user_input == "rock" and computer_pick == "scissors":
                    print("You won! .....")
                    break   
                    
                elif user_input == "scissors" and computer_pick == "paper":
                    print("You won! .......")
                    break    

                elif user_input == "paper" and computer_pick == "rock":
                    print("You won! .......")
                    break    
                
                else: 
                    print("You lost! The mage killed you as a result. Game over. ")
                    quit()
                    



            if answer == "blue book":
                answer = input("You continue on through a portal the mage opens to the other side of the wall. You have a choice of crossing a bridge or climbing down a ladder. Choose one. (bridge/ladder) ")
                if answer == "bridge":
                        print("You approach the unstable bridge slowly. Midway through the bridge snaps and collapses dropping you to your death. Game over. ")
                elif answer == "ladder":
                    answer = input("Climbing down the ladder leads you to what seems like a sewage system. You walk for what feels like miles until you reach the end of the sewage system. You find a red orb guarding an exit to what seems like the outside world. You pull out your book and turn through the blank pages until you find the only filled page which says 'shout BULOZAKUM for your freedom'. (BULOZAKUM) ")
                    if answer == "BULOZAKUM":
                            print("Congratulations! The orb guardian was destroyed and you exited the trecherous dungeon with your life! ")
                else: 
                     print("Invalid option. Game over.")

            elif answer == "red book":
                answer = input("You continue on through a portal the mage opens to the other side of the wall. You have a choice of crossing a bridge or climbing a ladder. Choose one. (bridge/ladder) ")
                if answer == "bridge":
                        print("You approach the unstable bridge slowly. Midway through the bridge snaps and collapses dropping you to your death. Game over. ")
                elif answer == "ladder":
                    answer = input("Climbing down the ladder leads you to what seems like a sewage system. You walk for what feels like miles until you reach the end of the sewage system. You find a red orb guarding an exit to what seems like the outside world. You pull out your book and turn through the blank pages until you find the only filled page which says 'shout Ruzambino for your freedom'. (RUZAMBINO) ")
                    if answer == "RUZAMBINO":
                            print("Oh no! The orb guardian was fueled with anger and you were slaughtered where you stood! Game over! ")
                else: 
                     print("Invalid option. Game over.")
            else:
                print("Invalid option. Game over.")
        elif answer == "return":
            print("You return to the cave area and hear rocks tumble down shutting each entrance you could go through. You're left to starve and die there with no exit. ")
        else: 
            print("Invalid option. Game over.")

    elif  answer == "right":
        print("You find a curved sword in this chest. The cave walls rumble and ghouls rise from the crevasses for you to fight. You fight with every bit of power you have but are overwhelmed and die as a result. ")
    else:
        print("Invalid option. Game over.")
else: 
     print("Invalid option. Game over.")