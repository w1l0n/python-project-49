import random
from brain_games.games.game_mechanics import welcome_user, play_round


def get_arithmetic_progression():
    a1 = random.randint(1, 11)
    r = random.randint(2, 5)
    n = 10

    progression = []
    for i in range(n):
        an = a1 + (r * i)
        progression.append(an)
    return progression


def hide_progression(progression):
    random_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    return progression, str(correct_answer)


def play_game():
    name = welcome_user()
    print("What number is missing in the progression?")

    correct_answer_count = 0
    while correct_answer_count < 3:
        progression = get_arithmetic_progression()
        modified_progression, correct_answer = hide_progression(progression)
        question = ' '.join(map(str, modified_progression))

        if play_round(question, correct_answer):
            correct_answer_count += 1
        else:
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
