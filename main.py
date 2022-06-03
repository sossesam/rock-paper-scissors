possible_options = ["R", "P","S"]

def game_play():
        comp = "S"

        while 1 == 1:
                user_choice = input("Select an option R for rock, P for paper, S for scissors : ")
                while user_choice not in possible_options:
                        print("you selected an invalid option")
                        user_choice  = input("Select an option R for rock, P for paper, S for scissors : ")
                        

                if user_choice == comp:
                        print("its a tie You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                
                elif user_choice == "R":
                        if comp == "P":
                                print("You Loss. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                        else:
                                print("You win. You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                                break

                




game_play()