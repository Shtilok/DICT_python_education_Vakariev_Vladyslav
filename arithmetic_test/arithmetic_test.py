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
        question = f"What is the square of {num}? "
        answer = num ** 2
    else:
        return "Invalid level"

    return question, answer


def increase_difficulty():
    print("Congratulations! You have passed level 1.")
    print("Would you like to proceed to level 2? Enter yes or no.")
    choice = input("> ").lower()
    if choice in ['yes', 'y']:
        return True
    else:
        return False


def save_results(name, level1_correct_answers, level2_correct_answers):
    total_correct_answers = level1_correct_answers + level2_correct_answers
    with open("results.txt", "a") as file:
        file.write(f"{name}: {total_correct_answers}/10 in levels 1 and 2\n")
    print("The results are saved in 'results.txt'.")


def main():
    print("Welcome to the Arithmetic Test!")

    level1_correct_answers = 0
    level2_correct_answers = 0
    level = 1

    # Проходження першого рівня
    for _ in range(5):
        question, answer = generate_question(level)
        user_answer = input(question + "\n> ")

        # Обробка введеної відповіді та перевірка на правильність
        while True:
            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Incorrect format.")
                user_answer = input("> ")

        if user_answer == answer:
            print("Right!")
            level1_correct_answers += 1
        else:
            print("Wrong!")

    # Вивід результатів проходження першого рівня
    print(f"Your mark for level 1 is {level1_correct_answers}/5.")

    # Підвищення рівня складності
    if level1_correct_answers >= 3:  # При проходженні 3 і більше завдань
        if increase_difficulty():
            level = 2

    # Проходження другого рівня
    if level == 2:
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
                level2_correct_answers += 1
            else:
                print("Wrong!")

        # Вивід результатів проходження другого рівня
        print(f"Your mark for level 2 is {level2_correct_answers}/5.")

    # Запит користувача на збереження результатів
    print("Would you like to save your results? Enter yes or no.")
    save_choice = input("> ").lower()
    if save_choice in ['yes', 'y']:
        name = input("What is your name?\n> ")
        save_results(name, level1_correct_answers, level2_correct_answers)


if __name__ == "__main__":
    main()
