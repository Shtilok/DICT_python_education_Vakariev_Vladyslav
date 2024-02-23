import random

def get_number_of_pencils():
    while True:
        try:
            num_pencils = int(input("How many pencils would you like to use:\n"))
            if num_pencils <= 0:
                print("The number of pencils should be positive")
            else:
                return num_pencils
        except ValueError:
            print("The number of pencils should be numeric")


def get_first_player():
    while True:
        first_player = input("Who will be the first player (John or Jack)?\n").capitalize()
        if first_player not in ['John', 'Jack']:
            print("Please choose between 'John' and 'Jack'")
        else:
            return first_player


def take_pencils(current_player, remaining_pencils):
    while True:
        try:
            if current_player == 'John':
                num_taken = int(input(f"{current_player}'s turn:\n"))
            else:  # Jack's turn
                if remaining_pencils % 4 == 0:
                    num_taken = random.randint(1, 3)
                else:
                    num_taken = remaining_pencils % 4
            if num_taken < 1 or num_taken > 3:
                print("Possible values: '1', '2' or '3'")
            elif num_taken > remaining_pencils:
                print("Too many pencils were taken")
            else:
                return num_taken
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def bot_turn(remaining_pencils):
    if remaining_pencils % 4 == 0:
        return random.randint(1, 3)
    else:
        return remaining_pencils % 4


def main():
    num_pencils = get_number_of_pencils()

    first_player = get_first_player()
    current_player = first_player

    while num_pencils > 0:
        print("|" * num_pencils)

        if current_player == 'John':
            num_taken = take_pencils('John', num_pencils)
            num_pencils -= num_taken
            if num_pencils <= 0:
                break
            current_player = 'Jack'
        else:
            if num_pencils <= 3:
                num_taken = num_pencils
            else:
                num_taken = bot_turn(num_pencils)
            num_pencils -= num_taken
            if num_pencils <= 0:
                break
            print(f"Jack's turn: {num_taken}")
            current_player = 'John'

    winner = 'John' if current_player == 'Jack' else 'Jack'
    print(f"{winner} won!")


if __name__ == "__main__":
    main()
