import random

def ask_number(nb_min, nb_max):
    number_int = 0
    while number_int == 0:
        number_str = input(f"What is the magic number (between {nb_min} and {nb_max}) ?")
        try:
            number_int = int(number_str)
        except:
            print("Please enter a number, try again.")
        else:
            if number_int < nb_min or number_int > nb_max:
                print(f"Please enter a number between {nb_min} and {nb_max}, try again.")
                number_int = 0

    return number_int


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4

# number = 0
# lives = NB_LIVES
# while not number == MAGIC_NUMBER and lives > 0:
#     number = ask_number(MIN_NUMBER, MAX_NUMBER)
#     print(f"You have {lives} lives")
#     if number == MAGIC_NUMBER:
#         print("You won!")
#     elif number > MAGIC_NUMBER:
#         print("The magic number is lower")
#         lives -= 1
#     else:
#         print("The magic number is greater")
#         lives -= 1
#
# if lives == 0:
#     print(f"You lost!,  the magic number was {MAGIC_NUMBER}")

win = False
for i in range(0, NB_LIVES):
    lives = NB_LIVES - i
    print(f"You have {lives} lives")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)

    if number == MAGIC_NUMBER:
        print("You won!")
        win = True
        break
    elif number > MAGIC_NUMBER:
        print("The magic number is lower")
    else:
        print("The magic number is greater")

if not win:
    print(f"You lost!,  the magic number was {MAGIC_NUMBER}")