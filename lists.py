# DaveGray: lists and tuples
users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-1])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users.sort()
print(users)
