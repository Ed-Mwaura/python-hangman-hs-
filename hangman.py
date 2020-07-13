# Write your code here
import random

my_list = ['python', 'java', 'kotlin', 'javascript']
random_choice = random.choice(my_list)

num = len(random_choice)

ascii_lowercase = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

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
    if len(letter) != 1:
        print("You should input a single letter\n")
    else:
        if letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter\n")

        else:
            if letter in random_choice:
                if letter not in chosen_letter:
                    print()
                    for i in range(0, num):
                        if random_choice[i] == letter:
                            dash_list[i] = random_choice[i]
                            chosen_letter.add(letter)

                else:
                    print("You already typed this letter\n")

            else:
                if letter in chosen_letter:
                    print("You already typed this letter\n")
                else:
                    print("No such letter in the word")
                    chosen_letter.add(letter)
                    tries -= 1
                    if tries == 0:
                        print("You are hanged!")
                    else:
                        print()
