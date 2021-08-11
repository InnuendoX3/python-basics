def run():
    lista = [19, 30, "Anything here", True, "Other thing"]
    print(lista)

    # append() add to the list -> like .push() in JS
    lista.append(False)
    print(lista)

    # pop() remove from the list, add the index
    lista.pop(1)
    print(lista)


if __name__ == "__main__":
    run()