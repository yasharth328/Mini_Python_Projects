import random
list_of_attempts = []
def your_score():
    if len(list_of_attempts) <= 0:
        print("No High Score,yet!")
    else:
        print("The current high score is {} attempts".format(min(list_of_attempts)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello,Welcome to Guess the Number")
    player_name = input("Enter Your Name:")
    play_wish = input("Hi, {}, would you like to play? (Enter Yes/No) ".format(player_name))
    attempts = 0
    your_score()
    while play_wish.lower() == "yes":
        try:
            guess = input("Try Guessing a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess within 1 to 10")
            if int(guess) == random_number:
                print("You guessed right!")
                attempts += 1
                list_of_attempts.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                your_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("Bye!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Invalid Value. Try again...")
            print("({})".format(err))
    else:
        print("Bye!")
if __name__ == '__main__':
    start_game()
