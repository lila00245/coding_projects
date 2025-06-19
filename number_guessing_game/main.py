import random

def main():

    print("welcome to the number guessing name, enter a range to start!")

    min_number: int = int(input("enter the minimum number: "))
    max_number: int = int(input("enter the maximum number: "))

    computer_guess : int = random.randint(min_number, max_number)
    print("okay, computer has chosen a number... ")

    win : bool = False
    number_of_guesses : int = 1

    while not win :
        user_guess : int = int(input("guess a number: "))

        if user_guess > computer_guess:
            print("incorrect, your number is too high, try again!")
            max_number = user_guess
            number_of_guesses += 1
        elif user_guess < computer_guess:
            print("incorrect, your number is too low, try again!")
            min_number = user_guess
            number_of_guesses += 1
        # otherwise, user has guessed correct number
        else:
            win = True

    # breaking loop..
    print(f"you have correctly guessed the number '{computer_guess}' in {number_of_guesses} guesses. congrats!")


if __name__ == "__main__":
    main()