name = "Dave"
count = 1

def another():
    color = "blue"
    count = 2
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting("Dave")

another()
