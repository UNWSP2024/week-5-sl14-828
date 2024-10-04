# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.

import random


def math_quiz():
    # Generate two random numbers between 1 and 999
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)


    correct_answer = num1 + num2

    # Display quiz
    print(f"  {num1}")
    print(f"+ {num2}")
    print("------")

    # Input
    user_answer = int(input("Your answer: "))

    # Check
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect")


if __name__ == '__main__':
    math_quiz()
