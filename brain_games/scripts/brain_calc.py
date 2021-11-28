#!/usr/bin/env python

import random
import prompt
import time

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')


def main():
    c = 0
    symb = list('+-*')
    start_of_range = 1
    end_of_range = 99
    while c < 4:
        rand_number_1 = random.randint(start_of_range, end_of_range)
        rand_number_2 = random.randint(start_of_range, end_of_range)
        z = random.choice(symb)
        print('What is the result of the expression?')
        print('Question:', rand_number_1, z, rand_number_2)
        answer = prompt.integer('Your answer: ')
        if z == '+':
            answ = rand_number_1 + rand_number_2
            if answer == answ:
                print('Correct!')
                c += 1
            else:
                print("'" + str(answer) + "'" + ' is wrong answer:(. Correct answer was ' + "'" + str(answ) + "'" + '.')
                print("Let's try again, " + name + '!')
                break
        elif z == '-':
            answ = rand_number_1 - rand_number_2
            if answer == answ:
                print('Correct!')
                c += 1
            else:
                print("'" + str(answer) + "'" + ' is wrong answer:(. Correct answer was ' + "'" + str(answ) + "'" + '.')
                print("Let's try again, " + name + '!')
                break
        else:
            answ = rand_number_1 * rand_number_2
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
