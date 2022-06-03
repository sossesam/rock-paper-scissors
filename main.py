possible_options = ["R", "P","S"]

def game_play():
        comp = "R"

        while 1 == 1:
                user_choice = " "
                while user_choice not in possible_options:
                        user_choice = input("Select an option R for rock, P for paper, S for scissors : ")

                if user_choice == comp:
                        print("its a tie You rolled:{}, and computer rolled: {}".format(user_choice, comp))
                
                



game_play()