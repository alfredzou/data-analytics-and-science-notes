def my_function(y):
    print("step_in_filler")
    print("step_in_filler")
    print("step_in_filler")
    print("step_in_filler")
    return y + 10


print(my_function(0))
print(my_function(1))
print(my_function(2))
print(my_function(3))
print(my_function(4))
print(my_function(5))


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
