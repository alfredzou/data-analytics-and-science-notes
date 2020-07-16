def add():
    x = int(input("Input first number: "))
    y = int(input("Input second number: "))
    print(f"The sum of {x} and {y} is {x + y}")


def sub():
    x = int(input("Input first number: "))
    y = int(input("Input second number: "))
    print(f"{x} subtracted by {y} is {x - y}")


# By using a while True loop, we can ask the program to listen for user inputs, until they decide to close it
while True:
    inp = input("Specify a function to run, add, sub or exit: ")
    if inp == "add":
        add()
    elif inp == "sub":
        sub()
    elif inp == "exit":
        exit()
