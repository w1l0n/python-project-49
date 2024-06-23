import random
from brain_games.games.game_mechanics import welcome_user, play_round


def get_gcd():
    value_one = random.randint(2, 25)
    value_two = random.randint(26, 50)

    value_one_orig, value_two_orig = value_one, value_two

    while value_two != 0:
        value_one, value_two = value_two, value_one % value_two
    result = value_one
    return value_one_orig, value_two_orig, result


def play_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    correct_answer_count = 0
    while correct_answer_count < 3:

        number_one, number_two, correct_answer = get_gcd()
        question = f'{number_one} {number_two}'

        correct_answer = str(correct_answer)

        if play_round(question, correct_answer):
            correct_answer_count += 1
        else:
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
