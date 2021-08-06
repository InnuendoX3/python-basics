def run():
    BASE = 2
    LIMIT = 1000
    
    exponent = 0
    power = BASE**exponent
    while power < LIMIT:
        print("The power of " + str(BASE) + " to exponent " + str(exponent) + " is " + str(power))
        exponent = exponent + 1
        power = BASE**exponent



if __name__ == "__main__":
    run()
