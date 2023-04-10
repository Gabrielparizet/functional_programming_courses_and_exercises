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