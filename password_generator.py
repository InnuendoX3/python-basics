import random

def generate_password():
    UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SYMB = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '^', '&', '$', '#']

    all_characters = UPPER*2 + LOWER*2 + NUMS + SYMB
    password = []

    for i in range(15):
        random_char = random.choice(all_characters)
        password.append(random_char)

    password = "".join(password)

    return password


def run():
    password = generate_password()
    print("This is your new password: " + password)


if __name__ == "__main__":
    run()