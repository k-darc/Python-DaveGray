name = "Dave"
count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        print(color)
        print(name)

    greeting("Dave")

another()
