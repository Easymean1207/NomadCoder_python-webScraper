from random import randint
from time import sleep


def pythonCasino():
    print("===== Play match game with your PC! =====")
    pc_choice = randint(1, 50)
    is_playing = True

    while is_playing:
        # only one argument in input()
        user_choice = int(input("Choose number (1~50):"))

        if user_choice == pc_choice:
            print(f"You won! Computer chose {pc_choice}")
            is_playing = False

        elif user_choice > pc_choice:
            print("Down! your choice is too high!")

        elif user_choice < pc_choice:
            print("Up! your choice is too low!")

        sleep(0.5)


pythonCasino()
