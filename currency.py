def conversor(type_pesos, dolar_value):
  pesos = float(input("¿Cuantos pesos " + type_pesos + " tienes? "))
  dolares = pesos / dolar_value
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $" + dolares + " dolares")


menu = """
¿Qué tipo de pesos quieres cambiar?

1. Pesos colombianos.
2. Pesos argentinos.
3. Pesos mexicanos.

Ingresa tu opción: """

option = int(input(menu))

if option == 1:
  conversor("colombianos", 3903)
elif option == 2:
  conversor("argentinos", 96.8)
elif option == 3:
  conversor("mexicanos", 19.9)
else:
  print("Enter a valid option.")