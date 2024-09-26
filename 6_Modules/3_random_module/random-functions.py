# Python offers random module that can generate random numbers.
import random
random_number = random.random()
print("Random Number:", random_number)

random_float = random.uniform(1.0, 10.0)
print("Random Floating-Point Number:", random_float)

random_integer = random.randint(1, 10)
print("Random Integer:", random_integer)

random_custom = random.randrange(10, 21, 2)
print("Random Custom Integer:", random_custom)

random_sequence = [random.randrange(1, 11) for _ in range(5)]
print("Random Sequence:", random_sequence)

random_even_sequence = [random.randrange(2, 21, 2) for _ in range(5)]
print("Random Even Sequence:", random_even_sequence)

random_odd_sequence = [random.randrange(1, 20, 2) for _ in range(5)]
print("Random Odd Sequence:", random_odd_sequence)

my_deck = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7"]
random.shuffle(my_deck)
print("Shuffled Deck:", my_deck)

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
random_colors = random.sample(colors, 3)
print("Random Colors:", random_colors)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
random_fruit = random.choice(fruits)
print("Random Fruit:", random_fruit)

options = ["candy", "chips", "fruit", "cookie"]
weights = [0.4, 0.2, 0.2, 0.2]
random_choices = random.choices(options, weights=weights, k=5)
print("Random Choices:", random_choices)

list=[2,4,5,3,6]
print(random.choice(list))
print(random.randint(5,13))
print(random.randint(-15,-13))

spinwheel=("5 gold coins", "5 silver coins", "1 diamond")
print(random.choices(spinwheel,[10,10,2],k=5))
print(random.choices(spinwheel,[10,0,10],k=3))
print(random.choices(spinwheel,[0,10,10],k=3))
print(random.choices(spinwheel,[0,10,0],k=3))

# Set a random seed
random.seed(45)
# Generate 5 random numbers
for i in range(5):
    print(random.randint(1, 100))