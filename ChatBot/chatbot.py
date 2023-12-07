print("Hello! My name is Your Favorite Bot.")
print("I was created in 2023.")
print("Please, remind me your name.")
user_input = input("My name is")
print("What a great name you have," + user_input + "!")
print("Let me guess your age.")
print(" Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = float(input("day->"))
remainder5 = float(input("month->"))
remainder7 = float(input("year->"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is, {age}; that's a good time to start programming!")
user_input = input("Be kind, enter a positive whole number: ")
if user_input.isdigit() and int(user_input) > 0:
    number = int(user_input)
    print("Counting from 0 to", number)
    for i in range(number + 1):
        print(i, end="!")
        print()
else:
    print("You entered an incorrect value. Please enter a positive integer.")
print("Let's test your programming knowledge.")
def run_programming_test():
    question = "Let's test your programming knowledge.\nWhy do we use methods?\n1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To determine the execution time of a program.\n4. To interrupt the execution of a program."
print("Why do use menthods")
while True:
    user_answer=input(">")
    if user_answer.isdigit() and int(user_answer) == 2:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")