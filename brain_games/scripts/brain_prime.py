#!/usr/bin/env python

import random
import prompt

print('Welcome to the Brain Games!')
NAME = prompt.string('May I have your name? ')
print('Hello, ' + NAME + '!')
print('Answer "yes" if given number is prime. Otherwise answer "no".')


START_OF_RANGE = 1
END_OF_RANGE = 100


def simple_num():
    '''Проверка простое ли число'''
    number = random.randint(START_OF_RANGE, END_OF_RANGE)
    text_question = f'{number}'
    count = 0
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            count += 1
    if count == 0 or number == 2:
        correct_answer = 'yes'
        return text_question, correct_answer
    correct_answer = 'no'
    return text_question, correct_answer


def main():
    c = 0
    while c < 4:
        text_question, correct_answer = simple_num()
        print(f'Question: {text_question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            c += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {NAME}!')
            break
        if c == 3:
            print(f'Congratulations, {NAME}!')
            break


if __name__ == '__main__':
    main()
