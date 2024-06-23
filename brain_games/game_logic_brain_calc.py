import random
from brain_games.game_mechanics import welcome_user, play_round


def generate_expression():
    value_one = random.randint(10, 20)
    value_two = random.randint(2, 9)
    operation = ['+', '-', '*']
    operation = random.choice(operation)

    if operation == '+':
        result = value_one + value_two
    elif operation == '-':
        result = value_one - value_two
    elif operation == '*':
        result = value_one * value_two
    return value_one, operation, value_two, result


def play_game():
    name = welcome_user()
    print("What is the result of the expression?")

    correct_answer_count = 0
    while correct_answer_count < 3:

        value_one, operation, value_two, correct_answer = generate_expression()
        question = f'{value_one}{operation}{value_two}'

        correct_answer = str(correct_answer)

        if play_round(question, correct_answer):
            correct_answer_count += 1
        else:
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
