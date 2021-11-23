#!/usr/bin/env python

import random
import prompt
import time

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello,', name)


def main():
    start_of_range = 1
    end_of_range = 99999
    c = 0
    while c < 4:
        rand_number = random.randint(start_of_range, end_of_range)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Ouestion:', rand_number)
        answer = prompt.string('Your answer: ')
        if rand_number % 2 == 0 and answer == 'yes':
            c += 1
        elif rand_number % 2 != 0 and answer == 'no':
            c += 1
        else:
            c = 0
            print("Let's try again,", name)
            print()
            time.sleep(3)
            continue
        if c == 3:
            print('Congratulations,', name)
            break
            


if __name__ == '__main__':
    main()
