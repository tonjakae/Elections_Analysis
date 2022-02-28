# Declare the temperature variable.  Wrap input statement in int() to convert string to integer.
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")