def run():
    # break interrupts the whole loop
    for i in range(100):
        print(i)
        if i == 67:
            break

    # print pair numbers
    # continue interrupts the loop and continue with the next
    for i in range(200):
        if i % 2 != 0:
            continue
        print(i)

    sentence = input("Write something: ")
    for character in sentence:
        if character == "o":
            break
        print(character)


if __name__ == "__main__":
    run()