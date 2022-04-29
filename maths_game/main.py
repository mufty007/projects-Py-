import random

# Constant
MIN_NUMBER = 1
MAX_NUMBER = 10
NB_QUESTIONS = 4


def ask_question():
    # Generate question

    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    o = random.randint(0, 1)
    # 0 -> +
    # 1 -> *
    operator_str = "+"

    if o == 1:
        operator_str = "*"
    c = input(f"Compute {a} {operator_str} {b} = ")
    c_int = int(c)
    compute = a+b
    if o == 1:
        compute = a * b
    if c_int == compute:
        return True

    return False


# asking more than 1 questions and pints
nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question no.{i + 1} out of {NB_QUESTIONS}")
    if ask_question():
        print("Right Answer!")
        nb_points += 1
    else:
        print("Wrong Answer!")
    print()

print(f"You got : {nb_points} out of {NB_QUESTIONS}")
average = int(NB_QUESTIONS/2)
if nb_points == NB_QUESTIONS:
    print("Excellent!")
elif nb_points == 0:
    print("Improve your maths!")
elif nb_points >= average:
    print("Good!")
else:
    print("You can do better")