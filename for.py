for i in range(1, 10):
  print("*** Multiplication table of " + str(i) + " ***")
  for j in range(0, 11):
    text = str(i) + " X " + str(j) + " = "
    print(text + str(i*j))
