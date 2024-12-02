import pandas as pd
import random
from option_generator import generate_options

def generate_and_ask_mcq_question(question_words,answer_words,question_answer_map):

    question_word = random.choice(question_words)
    correct_answer = question_answer_map[question_word]
    
    # options = [correct_answer]
    options = generate_options(correct_answer,answer_words)
    
    # # Add random incorrect answers to the options
    # while len(options) < x:
    #     incorrect_answer = random.choice(answer_words)
    #     if incorrect_answer not in options:
    #         options.append(incorrect_answer)
    
    # # Shuffle the options
    # random.shuffle(options)
    
    # Ask the user for the translation of the German word
    print(f"\033[33m What is the translation of '{question_word}'?\n\033[0m")
    
    # Show the options
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Get user's answer
    while True:
        try:
            answer = int(input("Choose the correct option (1-4): "))
            if options[answer - 1] == correct_answer:
                print("\033[32m\nCorrect! Well done.\n\033[0m")
                return (True,question_word)
            else:
                print(f"\033[31m\nIncorrect! The correct answer was: '{correct_answer}'.\n\033[0m")
                return (False,question_word)
        except (ValueError, IndexError):
            print("Invalid input. Please choose a number between 1 and 4.\n")
