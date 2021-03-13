nums = [11, 22, 33, 44, 55]

# takes a function and an iterable as arguments, and returns a new iterable with the funciton applied to each argument
result = list(map(lambda x: x+5, nums))
print(result)

# filters an iterable by removing items that don't match a predicate
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

