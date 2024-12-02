def check_correctness(answer,correct_answer):

    answer_in_slashes = correct_answer.split("/")

    for correct_answer in answer_in_slashes:        
        isCorrectInLowercase = answer.lower().strip() == correct_answer.lower().strip()
        isCorrectWithAddingThe = "the " + answer.lower() == correct_answer.lower().strip()
        isCorrectWithRemovingThe = answer.lower() == "the " + correct_answer.lower().strip()
        if isCorrectInLowercase or isCorrectWithAddingThe or isCorrectWithRemovingThe :
            return True

    return False
