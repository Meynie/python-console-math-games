#!/usr/bin/env python

import random
import prompt
import time

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello,', name)


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


def main():
    c = 0
    while c < 4:
        lis = posl()
        iscl = random.randint(0, len(lis))
        a = lis[iscl - 1]
        lis.insert(iscl, '..')
        if iscl != 0:
            lis.pop(iscl - 1)
        elif iscl == 0:
            lis.pop(iscl + 1)
        print('What number is missing in the progression?')
        print('Ouestion:', *lis)
        answer = prompt.integer('Your answer: ')
        if answer == a:
            print('Correct!')
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
