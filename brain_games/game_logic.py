from random import randint
import prompt


def is_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('"Answer "yes" if the number is even, otherwise answer "no"."')

    correct_answer = 0

    while correct_answer < 3:

        random_value = randint(1, 100)
        print(f"Question: {random_value}")
        user_input = input().lower()
        is_even = (random_value % 2 == 0)

        if (is_even and user_input == 'yes') or (not is_even and user_input == 'no'):
            print('Correct!')
            correct_answer += 1
        else:
            if not is_even:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}")
