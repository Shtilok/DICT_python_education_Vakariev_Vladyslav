import random


def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, num1)  # Змінено діапазон для num2, щоб не було від'ємних відповідей
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        answer = eval(question)
    elif level == 2:
        num = random.randint(11, 29)
        question = f"{num}"
        answer = num ** 2  # Возводим число в квадрат
    else:
        return "Invalid level"

    return question, answer


def main():
    correct_answers = 0

    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    while True:
        try:
            level = int(input("> "))
            if level in [1, 2]:
                break
            else:
                print("Invalid level. Enter 1 or 2.")
        except ValueError:
            print("Invalid input. Enter a number.")

    for _ in range(5):
        question, answer = generate_question(level)
        user_answer = input(question + "\n> ")

        while True:
            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Incorrect format.")
                user_answer = input("> ")

        if user_answer == answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    save_result = input("> ").lower()

    if save_result in ['yes', 'y', 'YES', 'Yes']:
        name = input("What is your name?\n> ")
        with open("results.txt", "a") as file:
            file.write(
                f"{name}: {correct_answers}/5 in level {level} ({'simple operations with numbers 2-9' if level == 1 else 'integral squares of 11-29'})\n")
        print("The results are saved in 'results.txt'.")


if __name__ == "__main__":
    main()
