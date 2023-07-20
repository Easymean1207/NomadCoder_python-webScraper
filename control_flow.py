import random
import time

print("Welcome to Python Casino!")
pc_choice = random.randint(1, 50)
is_playing = True

while is_playing:
    # only one argument in input()
    user_choice = int(input("Choose number (1~50): "))

    if user_choice == pc_choice:
        print("You won!")
        is_playing = False

    elif user_choice > pc_choice:
        print("Lower! your choice is too high!")

    elif user_choice < pc_choice:
        print("Higher! your choice is too low!")

    time.sleep(0.5)
