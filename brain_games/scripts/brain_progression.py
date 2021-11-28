#!/usr/bin/env python

import random
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')


def posl():
    '''Генерация случайной арифметической прогрессии'''
    start_of_range = 1
    end_of_range = 100
    start_of_range_step = 1
    end_of_range_step = 10
    posl = []
    rand_number = random.randint(start_of_range, end_of_range)
    step = random.randint(start_of_range_step, end_of_range_step)
    posl.append(rand_number)
    for i in range(1, 10):
        posl.append(rand_number + step)
        rand_number += step
    return posl


print('What number is missing in the progression?')


def main():
    c = 0
    while c < 4:
        lis = posl()
        iscl = random.randint(0, len(lis) - 1)
        a = lis[iscl]
        lis.insert(iscl, '..')
        lis.pop(iscl + 1)
        print('Question:', *lis)
        answer = prompt.integer('Your answer: ')
        if answer == a:
            print('Correct!')
            c += 1
        elif answer != a:
            c = 0
            print("'" + str(answer) + "'" + ' is wrong answer:(.')
            print('Correct answer was ' + "'" + str(a) + "'" + '.')
            print("Let's try again, " + name + '!')
            break
        if c == 3:
            print('Congratulations, ' + name + '!')
            break


if __name__ == '__main__':
    main()
