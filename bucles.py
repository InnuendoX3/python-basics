def run(exponent):
    base = 2
    result = base ** exponent
    base_str = str(base)
    exponent_str = str(exponent)
    result_str = str(result)
    if(result <= 1000):
        print(base_str + " a la " + exponent_str + " = " + result_str)
        run(exponent + 1)
    else:
        print("The end")


if __name__ == "__main__":
    run(2)
