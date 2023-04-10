# Exercise 1. Try rewriting the code below as a map. It takes a list of real names and replaces them with code names produced using a more robust strategy.
names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print(names)
# => [6306819796133686941, 8135353348168144921, -1228887169324443034]

# As a map:
hashed_names = list(map(lambda x: hash(x), names))
print(hashed_names)
# Other solution 
# hashed_names = map(hash, names)



# Exercise 2. Try rewriting the code below using map, reduce and filter.
people = [{'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print(average_height)
    # => 120

# Solution:
from functools import reduce
from operator import add
people_with_heights = list(filter(lambda x: 'height' in x, people))
print(people_with_heights)
heights = list(map(lambda x: x['height'], people_with_heights))
print(heights)
average_height = reduce(add, heights) / len(heights)
print('average height: ', average_height)

# Correction:
heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))

if len(heights) > 0:
    average_height = reduce(add, heights) / len(heights)