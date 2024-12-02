import random
from correctness import check_correctness
def generate_and_ask_word(question_words,question_answer_map):
    question_word = random.choice(question_words)
    # question_word = "to register"
    correct_answer = question_answer_map[question_word].split('(')[0].split(',')[0]
    
    answer = input(f"\033[33m What is the translation of '{question_word}'?\n\033[0m")

    if check_correctness(answer,correct_answer):
        print("\033[32m\nCorrect! Well done.\n\033[0m")
        return (True,question_word)
    else:
        print(f"\033[31m\nIncorrect! The correct answer was: '{correct_answer.strip()}'.\n\033[0m")
        return (False,question_word)


