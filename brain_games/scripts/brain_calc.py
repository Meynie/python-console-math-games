#!/usr/bin/env python

import random
import prompt

print('Welcome to the Brain Games!')
NAME = prompt.string('May I have your name? ')
print('Hello, ' + NAME + '!')
print('What is the result of the expression?')

OPERATOR = list('+-*')
START_OF_RANGE = 0
END_OF_RANGE = 90


def random_operator():
    number_1 = random.randint(START_OF_RANGE, END_OF_RANGE)
    number_2 = random.randint(START_OF_RANGE, END_OF_RANGE)
    operator = random.choice(OPERATOR)
    text_question = f'{number_1} {operator} {number_2}'
    if operator == '+':
        correct_answer = number_1 + number_2
        return text_question, correct_answer
    elif operator == '-':
        correct_answer = number_1 - number_2
        return text_question, correct_answer
    correct_answer = number_1 * number_2
    return text_question, correct_answer


def main():
    c = 0
    while c < 4:
        text_question, correct_answer = random_operator()
        print(f'Question: {text_question}')
        user_answer = prompt.integer('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
            c += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {NAME}!')
            break
        if c == 3:
            print('Congratulations, ' + NAME + '!')
            break


if __name__ == '__main__':
    main()
