value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is not equal to " + str(value))