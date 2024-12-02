import pandas as pd
import random
from mcq import generate_and_ask_mcq_question
from word import generate_and_ask_word
from correctness import check_correctness 
from configs import FILE_NAME,LANGUAGE_TO_ANSWER,QUESTION_TYPE,NUMBER_OF_QUESTIONS

# Load the Excel file
df = pd.read_excel(FILE_NAME)


# Assuming the first column contains German words and the second column contains English words
# Adjust the column names or indices if necessary
german_words = df.iloc[:, 0].tolist()  # List of German words
english_words = df.iloc[:, 1].tolist()  # List of English words

# Create a dictionary (hashmap) of German-English pairs

def create_quiz():
    correct_answer = 0
    incorrect_answer = 0
    incorrect_questions_list = []

    if LANGUAGE_TO_ANSWER == "German":
        question_words = english_words
        answer_words = german_words
        question_answer_map = dict(zip(english_words,german_words))

    elif LANGUAGE_TO_ANSWER == "English":
        question_words = german_words
        answer_words = english_words
        question_answer_map = dict(zip(german_words,english_words))

    for i in range(0,NUMBER_OF_QUESTIONS):

        print(f"\033[34m \n{i+1}/{NUMBER_OF_QUESTIONS} \n\033[0m")

        if QUESTION_TYPE == "MCQ":
            (isCorrect,question_word) = generate_and_ask_mcq_question(question_words,answer_words,question_answer_map)
        elif QUESTION_TYPE == "WORD":
            (isCorrect,question_word) = generate_and_ask_word(question_words,question_answer_map)

        if isCorrect:
            correct_answer += 1
        else:
            incorrect_questions_list.append(question_word)
            incorrect_answer += 1
        
        question_words.remove(question_word)
        
        print(f"correct: \033[32m{correct_answer}\033[0m incorrect: \033[31m{incorrect_answer}\033[0m\n")
        
    print("Repeating the incorrect question")
    
    while incorrect_questions_list != []:
        if QUESTION_TYPE == "MCQ":
            (isCorrect,question_word) = generate_and_ask_mcq_question(incorrect_questions_list,answer_words,question_answer_map)
        elif QUESTION_TYPE == "WORD":
            (isCorrect,question_word) = generate_and_ask_word(incorrect_questions_list,question_answer_map)

        if isCorrect:
            incorrect_questions_list.remove(question_word)
            print(f"{len(incorrect_questions_list)} words left")


    



# Run the quiz
if __name__ == "__main__":
    create_quiz()

