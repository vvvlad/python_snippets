def add_func(z): return z ** 2
def is_odd(z): return z % 2 == 1
def multiply(x, y): return x*y


aList = list(range(10))
print(aList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Syntax of list comprehension
# [expression(x) for x in aList if optional_condition(x)]


print(list(map(add_func, aList)))
print([x ** 2 for x in aList])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(filter(is_odd, aList)))
print([x for x in aList if x % 2 == 1])
# [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9]

# ============================================================= more examples

# Condition criterion
# [expression for item in iterable if condition]
 # The same list of integers
integers = [1, 2, 3, 4, 5, 6]
 # Create a list of squares for even numbers only
squares_of_evens = [x*x for x in integers if x % 2 == 0]
print((squares_of_evens))
# [4, 16, 36]


# Conditional exprecsions
# [expression0 if condition else expression1 for item in iterable]
 # The list of integers
integers = [1, 2, 3, 4, 5, 6]
 # Create a list of numbers, when the item is even, take the square
 # when the item is odd, take the cube
custom_powers = [x*x if x % 2 == 0 else pow(x, 3) for x in integers]
print(custom_powers)
# [1, 4, 27, 16, 125, 36]

# Nested
# [expression for item_outer in iterable for item_inner in item_outer]

# Equivalent to
# for item_outer in iterable:
#     for item_inner in item_outer:
#         expression


 # A list of tuples
prices = [('$5.99', '$4.99'), ('$3.5', '$4.5')]
 # Flattened list of prices
prices_formatted = [float(x[1:]) for price_group in prices for x in price_group]
print(prices_formatted)
# [5.99, 4.99, 3.5, 4.5]
