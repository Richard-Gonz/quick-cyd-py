import random

questions= [
    {
    "question": "Which animal has the strongest bite force of any living animal?",
    "correct_answer": "Saltwater Crocodile",
    "incorrect_answers":
    [
        "Great White Shark",
        "Nile Crocodile",
        "Hippopotamus"
    ]
},
 {
    "question": "What is the only mammal capable of true flight??",
    "correct_answer": "Bat",
    "incorrect_answers":
    [
        "Sugar Glider",
        "Flying Squirrel",
        "Pterosaur"
    ]
},
 {
    "question": "Which animal can survive complete decapitation for several days?",
    "correct_answer": "Cockroach",
    "incorrect_answers":
    [
        "Earthworm",
        "Starfish",
        "Frog"
    ]
},
 {
    "question": "Which country has the most time zones?",
    "correct_answer": "France",
    "incorrect_answers":
    [
        "Russia",
        "USA",
        "China"
    ]
},
 {
    "question": "What is the deepest point in the world’s oceans?",
    "correct_answer": "Mariana Trench",
    "incorrect_answers":
    [
        "Tonga Trench",
        "Philippine Trench",
        "Puerto Rico Trench"
    ]
},
 {
    "question": "Which desert is considered the driest place on Earth?",
    "correct_answer": "Atacama Desert",
    "incorrect_answers":
    [
        "Sahara Desert",
        "Gobi Desert",
        "Kalahari Desert"
    ]
},
 {
    "question": "Which element is liquid at room temperature?",
    "correct_answer": "Mercury",
    "incorrect_answers":
    [
        "Bromine",
        "Gallium",
        "Chlorine"
    ]
},
 {
    "question": "What is the second most abundant gas in the Earth’s atmosphere?",
    "correct_answer": "Oxygen",
    "incorrect_answers":
    [
        "Carbon Dioxide",
        "Argon",
        "Nitrogen"
    ]
},
 {
    "question": "Which planet has the fastest rotation (shortest day) in the Solar System?",
    "correct_answer": "Jupiter",
    "incorrect_answers":
    [
        "Saturn",
        "Neptune",
        "Mars"
    ]
},
 {
    "question": "Who was the first woman to win a Nobel Prize?",
    "correct_answer": "Marie Curie",
    "incorrect_answers":
    [
        "Rosalind Franklin",
        "Jane Goodall",
        "Ada Lovelace"
    ]
},
 {
    "question": "Which ancient civilization built the city of Machu Picchu?",
    "correct_answer": "Inca",
    "incorrect_answers":
    [
        "Maya",
        "Aztec",
        "Olmec"
    ]
},
 {
    "question": "During which century did the Black Death peak in Europe?",
    "correct_answer": "The 14th Century",
    "incorrect_answers":
    [
        "The 13th Century",
        "The 15th Century",
        "The 12th Century"
    ]
}
]
def  ask_question(question_data):
    answers = question_data["incorrect_answers"] + [question_data["correct_answer"]]
    random.shuffle(answers)
    choices = ['A', 'B', 'C', 'D']
    answers_dict = dict(zip(choices, answers))

    # Print out the question and answer
    print(question_data['question'])
    for letter, answer in answers_dict.items():
        print(f'{letter}: {answer}')

    while True:
        
        player_answer = input().upper()
        
        if player_answer in choices:
            break
        else:
            print(f"{player_answer} isn't a valid answer, try again")
                  
    if answers_dict[player_answer] == question_data['correct_answer']:
        print('Correct! +1 Point')
    else:
        print('Wrong! Next question...')
for question in questions:
    ask_question(question)