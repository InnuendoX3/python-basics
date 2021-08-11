def run():
    population_countries = {
        "Argentina": 44_938_712,
        "Brasil": 210_147_125,
        "Colombia": 50_352_424
    }

    print(population_countries)
    print(population_countries["Colombia"])
    
    # Loop and print keys
    for country in population_countries.keys():
        print(country)

    # Loop and print values
    for country in population_countries.values():
        print(country)
    
    # Loop and print both
    for country, population in population_countries.items():
        print(country + " has " + str(population) + " people.")



if __name__ == "__main__":
    run()