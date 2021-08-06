def is_palindrome(sentence):
    sentence = sentence.replace(" ", "").lower()
    sentence_reversed = sentence[::-1]
    if sentence == sentence_reversed:
        return True
    else:
        return False



def main():
    sentence = input("Enter a word or a sentence: ")
    if is_palindrome(sentence):
        print("Is a palindrome")
    else:
        print("Is not a palindrome")


if __name__ == "__main__":
    main()