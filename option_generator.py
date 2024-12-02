from configs import NUMBER_OF_OPTIONS
import random
import difflib

def generate_options(correct_answer, answer_words):
    options = [correct_answer]
    
    word_similarities = []
    for word in answer_words:
        similarity = difflib.SequenceMatcher(None, correct_answer, word).ratio()
        word_similarities.append((word, similarity))
    
    word_similarities.sort(key=lambda x: x[1], reverse=True)
    
    for word, _ in word_similarities:
        if len(options) >= NUMBER_OF_OPTIONS:
            break
        if word != correct_answer and word not in options:
            options.append(word)
    
    random.shuffle(options) 
    return options