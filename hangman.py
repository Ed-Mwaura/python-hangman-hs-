# Write your code here
import random

my_list = ['python', 'java', 'kotlin', 'javascript']
random_choice = random.choice(my_list)

num = len(random_choice)

dashes = "-" * num
dash_list = list(dashes)

hidden_word = random_choice[:3:] + dashes

print("H A N G M A N\n")

tries = 0
while tries < 8:
    print("".join(dash_list))
    letter = input("Input a letter: ")
    if letter in random_choice:
        for i in range(0, num):
            if random_choice[i] == letter:
                dash_list[i] = random_choice[i]
        print()
    else:
        print("No such letter in the word\n")
    tries += 1

print("Thanks for playing!")
print("We'll see how well you did in the next stage")