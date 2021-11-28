#!/usr/bin/env python

import random
import prompt

print('Welcome to the Brain Games!')
NAME = prompt.string('May I have your name? ')
print('Hello, ' + NAME + '!')
print('Answer "yes" if given number is prime. Otherwise answer "no".')


START_OF_RANGE = 1
END_OF_RANGE = 100


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
    if simple_num is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    c = 0
    while c < 4:
        num = random.randint(START_OF_RANGE, END_OF_RANGE)
        print('Question:', num)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            c += 1
            print('Correct!')
        elif answer != correct_answer:
            c = 0
            print("'" + str(answer) + "'" + " is wrong answer:(.")
            print("Correct answer was " + "'" + correct_answer + "'.")
            print("Let's try again, " + NAME + '!')
            break
        if c == 3:
            print('Congratulations, ' + NAME + '!')
            break


if __name__ == '__main__':
    main()
