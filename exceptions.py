x = 2
try:
    print(x / 0)
except NameError:
    print("NameError means something is probably undefined")
except ZeroDivisionError:
    print("Dividing by zero ends the universe")
