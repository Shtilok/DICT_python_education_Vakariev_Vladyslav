import random


def generate_question():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, num1)  # Змінено діапазон для num2, щоб не було від'ємних відповідей
    operator = random.choice(['+', '-', '*'])

    question = f"{num1} {operator} {num2}"
    answer = eval(question)

    return question, answer


def main():
    correct_answers = 0

    for _ in range(5):
        question, answer = generate_question()
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

    print(f"Your mark is {correct_answers}/5.")


if __name__ == "__main__":
    main()
