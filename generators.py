# The yield statement is used to define a generator, replacing the return of a function to provide a result to its
# caller without destroying local variables.


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)

# search decorators on yt
# python set dictionaries list what are those, itertools