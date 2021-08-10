def is_prime(number):
    for counter in range(1, number + 1):
        if number % counter == 0 and (counter != 1 and counter != number):
            print(counter)
            return False
    return True



def run():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(str(number) + " is a prime number")
    else:
        print(str(number) + " is not a prime number")


if __name__ == "__main__":
    run()