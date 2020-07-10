# Write your code here
import random

my_list = ['python', 'java', 'kotlin', 'javascript']
random_choice = random.choice(my_list)

num = len(random_choice)

dashes = "-" * num
dash_list = list(dashes)

print("H A N G M A N\n")

chosen_letter = set()
tries = 8
while tries > 0:
    answer_so_far = "".join(dash_list)

    print(answer_so_far)
    if answer_so_far == random_choice:
        print("You guessed the word")
        print("You survived!")
        break

    letter = input("Input a letter: ")
    if letter in random_choice:
        if letter not in chosen_letter:
            print()
            for i in range(0, num):
                if random_choice[i] == letter:
                    dash_list[i] = random_choice[i]
                    chosen_letter.add(letter)

        else:
            print("No improvements")
            tries -= 1
            if tries == 0:
                print("You are hanged!")
            else:
                print()

    else:
        print("No such letter in the word")
        tries -= 1
        if tries == 0:
            print("You are hanged!")
        else:
            print()


