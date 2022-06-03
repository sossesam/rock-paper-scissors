import random


possible_options = ["R", "P","S"]

def game_play():
        

        while 1 == 1:
                comp = random.choice(possible_options)
                user_choice = input("Select an option R for rock, P for paper, S for scissors : ").upper()
                while user_choice not in possible_options:
                        print("you selected an invalid option")
                        user_choice  = input("Select an option R for rock, P for paper, S for scissors : ").upper()
                        

                if user_choice == comp:
                        print("its a tie You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                
                elif user_choice == "R":
                        if comp == "P":
                                print("You Loss. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                        else:
                                print("You win. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                                break
                
                elif user_choice == "P":
                        if comp == "R":
                                print("You win. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                                break
                        else:
                                print("You loss. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                
                elif user_choice == "S":
                        if comp == "P":
                                print("You win. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                                break
                        else:
                                print("You loss. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                                
                

                




game_play()