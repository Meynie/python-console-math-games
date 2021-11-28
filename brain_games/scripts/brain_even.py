#!/usr/bin/env python

import random
import prompt

print('Welcome to the Brain Games!')
NAME = prompt.string('May I have your name? ')
print('Hello,', NAME)
print('Answer "yes" if the number is even, otherwise answer "no".')

START_OF_RANGE = 0
END_OF_RANGE = 99999


def even():
    rand_number = random.randint(START_OF_RANGE, END_OF_RANGE)
    text_question = f'{rand_number}'
    if rand_number % 2 == 0:
        correct_answer = 'yes'
        return text_question, correct_answer
    correct_answer = 'no'
    return text_question, correct_answer


def main():
    c = 0
    while c < 4:
        text_question, correct_answer = even()
        print(f'Question: {text_question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            c += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            break
        if c == 3:
            print('Congratulations, ' + NAME + '!')
            break


if __name__ == '__main__':
    main()
