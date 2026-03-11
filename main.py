import random

questions= {
    "question": "Which animal has the strongest bite force of any living animal?",
    "correct_answer": "Saltwater Crocodile",
    "incorrect_answers":
    [
        "Great White Shark",
        "Nile Crocodile",
        "Hippopotamus"
    ]
}
for question_data in question_data:
    ask_question(question_data)

# Make a list of the correct and incorrect answers
answers = question_data["incorrect_answers"] + [question_data["correct_answer"]]
# Randomize the list order so the correct answer isn’t always last
random.shuffle(answers)

# Make a dictionary where
choices = ['A', 'B', 'C', 'D']
answers_dict = dict(zip(choices, answers))

# Print out the question and answer
print(question_data['question'])
for letter, answer in answers_dict.items():
    print(f'{letter}: {answer}')

while True:
    # Get the player’s answer, make it uppercase so that ‘a’ will select the ‘A’ answer
    player_answer = input().upper()
    # Make sure the player’s answer is a valid choice
    if player_answer in choices:
        break
    else:
        print(f"{player_answer} isn't a valid answer, try again")

# Check if the dictionary answer the player chose matches the correct answer
if answers_dict[player_answer] == question_data['correct_answer']:
    print('Correct! +1 Point')
else:
    print('Wrong! Next question...')
