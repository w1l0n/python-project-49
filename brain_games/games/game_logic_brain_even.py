from random import randint
from brain_games.games.game_mechanics import welcome_user, play_round


def play_game():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answer_count = 0
    while correct_answer_count < 3:
        random_value = randint(1, 100)
        is_even = (random_value % 2 == 0)
        question = random_value

        correct_answer = 'yes' if is_even else 'no'
        if play_round(question, correct_answer):
            correct_answer_count += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
