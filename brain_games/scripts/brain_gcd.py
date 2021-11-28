#!/usr/bin/env python

import random
import prompt
import time

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')


def max_del(a, b):
    largest = -1
    min_n = min(a, b)
    for i in range(1, min_n + 1):
        if a % i == 0 and b % i == 0:
            if i > largest:
                largest = i
    return largest


def main():
    start_of_range = 1
    end_of_range = 99
    c = 0
    while c < 4:
        rand_number_1 = random.randint(start_of_range, end_of_range)
        rand_number_2 = random.randint(start_of_range, end_of_range)
        print('Find the greatest common divisor of given numbers')
        print('Question:', rand_number_1, rand_number_2)
        answer = prompt.integer('Your answer: ')
        answ = max_del(rand_number_1, rand_number_2)
        if answer == answ:
            print('Correct!')
            c += 1
        else:
            print("'" + str(answer) + "'" + ' is wrong answer:(. Correct answer was ' + "'" + str(answ) + "'" + '.')
            print("Let's try again, " + name + '!')
            break
        if c == 3:
            print('Congratulations, ' + name + '!')
            break


if __name__ == '__main__':
    main()
