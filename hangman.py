# Write your code here
import random

my_list = ['python', 'java', 'kotlin', 'javascript']
random_choice = random.choice(my_list)

num = len(random_choice)

dashes = "-" * (num)
print(dashes)

hidden_word = random_choice[:3:] + dashes

print("H A N G M A N")
print(dashes)
word = input()

if word == random_choice:
    print("You survived!")
else:
    print("You are hanged!")
