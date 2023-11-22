def squared(num): return num * num
# lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2
# def addTwo(num): return num + 2 - this is the auto formatting for VSCode's opt in beta.

print(addTwo(12))

sum = lambda a, b : a + b

print(sum(2, 2))

#################################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

##########################
# Higher Order Functions

numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

