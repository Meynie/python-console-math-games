#!/usr/bin/env python

import random
import prompt
import time

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello,', name)


def simple_num(num):
    '''Проверка простое ли число'''
    count = 0
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            count += 1
    if count == 0 or num == 2:
        return True
    else:
        return False


def main():
    c = 0
    while c < 4:
        start_of_range = 1
        end_of_range = 100
        num = random.randint(start_of_range, end_of_range)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print('Ouestion:', num)
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and simple_num(num) is True:
            c += 1
            print('Correct!')
        elif answer == 'no' and simple_num(num) is False:
            c += 1
            print('Correct!')
        else:
            c = 0
            print("Let's try again,", name)
            print(simple_num(num))
            break
        if c == 3:
            print('Congratulations,', name)
            break


if __name__ == '__main__':
    main()
