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
        first_player = input("Who will be the first (John, Jack):\n")
        if first_player.lower() not in ['john', 'jack']:
            print("Choose between 'John' and 'Jack'")
        else:
            return first_player


def take_pencils(current_player, remaining_pencils):
    while True:
        try:
            num_taken = int(input(f"{current_player}'s turn:\n"))
            if num_taken < 1 or num_taken > 3:
                print("Possible values: '1', '2' or '3'")
            elif num_taken > remaining_pencils:
                print("Too many pencils were taken")
            else:
                return num_taken
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def main():
    num_pencils = get_number_of_pencils()
    current_player = get_first_player()

    while num_pencils > 0:
        print("|" * num_pencils)

        num_taken = take_pencils(current_player, num_pencils)
        num_pencils -= num_taken

        if num_pencils <= 0:
            break

        # Зміна поточного гравця
        current_player = 'Jack' if current_player == 'John' else 'John'

    winner = 'John' if current_player == 'Jack' else 'Jack'
    print(f"{winner} won!")


if __name__ == "__main__":
    main()
