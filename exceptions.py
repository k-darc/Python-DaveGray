x = 2
try:
    raise NotCoolError("Not cool!!")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Dividing by zero ends the universe. Don't do this.")
else:
    print("No errors!")
finally:
    print("I'm going to print with or without an error.")