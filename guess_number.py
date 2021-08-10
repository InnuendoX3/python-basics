import random

def run():
    secret_number = random.randint(1, 100)
    user_number = int(input("Choose a number between 1 and 100: "))
    while user_number != secret_number:
        if user_number < secret_number:
            user_number = int(input("Pick a bigger number: "))
        else:
            user_number = int(input("Pick a smaller number: "))
    print("Yeah! You guessed the number!")


if __name__ == "__main__":
    run()