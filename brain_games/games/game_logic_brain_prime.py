import random
from brain_games.games.game_mechanics import welcome_user, play_round


def get_random():
    return random.randint(2, 20)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answer_count = 0
    while correct_answer_count < 3:

        question = get_random()
        correct_answer = 'yes' if is_prime(question) else 'no'

        if play_round(question, correct_answer):
            correct_answer_count += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

play_game()