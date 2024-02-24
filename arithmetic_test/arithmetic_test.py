import random


def generate_question():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operator = random.choice(['+', '*', '-'])

    if operator == '-':
        # Гарантуємо, що результат віднімання не буде від'ємним
        num1, num2 = max(num1, num2), min(num1, num2)

    question = f"{num1} {operator} {num2}"
    answer = eval(question)

    return question, answer


def main():
    question, answer = generate_question()
    user_answer = input(question + "\n> ")

    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Please enter a valid integer.")
        return

    if user_answer == answer:
        print("Right!")
    else:
        print("Wrong!")


if __name__ == "__main__":
    main()
