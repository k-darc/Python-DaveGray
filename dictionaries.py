# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page") # With constructor function

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key.value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# band2 = band # creates a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dictionary constructor function
band3 = dict(band)
print("Good copy!")
print(band3)