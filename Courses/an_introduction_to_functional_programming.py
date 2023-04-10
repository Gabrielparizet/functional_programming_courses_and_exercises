# This course is based on the article "An introduction to functional programming" by Mary Rose Cook
# https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming

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


# This code counts how often the word ‘Sam’ appears in a list of strings:
sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

sam_count = 0
for sentence in sentences:
    sam_count += sentence.count('Sam')

print(sam_count)
# => 3


# Same code written as a reduce:
sam_count = reduce(lambda a, x: a + x.count('Sam'), sentences, 0)
print(sam_count)



# Write declaratively, not imperatively
# from random import random

# time = 5
# car_positions = [1, 1, 1]

# while time:
#     # decrease time
#     time -= 1

    # print('')
    # for i in range(len(car_positions)):
    #     # move car
    #     if random() > 0.3:
    #         car_positions[i] += 1

        # draw car
        # print('-' * car_positions[i])


# More declarative programming:
from random import random

def move_cars():
    for i, _ in enumerate(car_positions):
        if random() > 0.3:
            car_positions[i] += 1

def draw_car(car_position):
    print('-' * car_position)

def run_step_of_race():
    global time
    time -= 1
    move_cars()

def draw():
    print('')
    for car_position in car_positions:
        draw_car(car_position)

time = 5
car_positions = [1, 1, 1]

while time:
    run_step_of_race()
    draw()

