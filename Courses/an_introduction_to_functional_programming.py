# UNFUNCTIONAL:
a = 0
def increment1():
    global a
    a += 1

# FUNCTIONAL:
def increment1(a):
    return a + 1



# Map
name_lengths = list(map(len, ["Mary", "Gabriel", "Olivia"]))
print(name_lengths)
# => [4, 7, 6]

squares = list(map(lambda x: x*x, [0, 1, 2, 3, 4]))
print(squares)
# => [0, 1, 4, 9, 16]



# UNFUNCTIONAL
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print(names)
# => ['Mr. Blonde', 'Mr. Blonde', 'Mr. Blonde']

# Rewritten as a map
import random

names = ['Mary', 'Isla', 'Sam']

secret_names = list(map(lambda x: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']), names))
print(secret_names)



# Reduce
from functools import reduce
sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(sum)
# => 10