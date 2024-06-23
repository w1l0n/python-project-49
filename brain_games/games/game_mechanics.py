import prompt


def welcome_user():
    print("Welcome to the Brain games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def ask_question(question):
    print(f'Question: {question}')
    return prompt.string('Your answer: ')


def play_round(question, correct_answer):
    user_answer = ask_question(question)
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        return False
