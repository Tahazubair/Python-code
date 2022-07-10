from Questions import Questions
Question_prompt = [
    "Multan is Known As?\n a) Mooltan \n b) City of Saints \n c) Molten \n\n",
    "Multan's most famous thing?\n a) Sohn Halwa \n b) cold  \n c) roads \n\n",
    "Multan famous for?\n a) food \n b) Dust \n c) Pottery \n\n"
]
test_questions = [
    Questions(Question_prompt[0], "b"),
    Questions(Question_prompt[1], "a"),
    Questions(Question_prompt[2], "c")
]


def run(test_questions):
    score = 0
    for question in test_questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(test_questions)) + " correct")


run(test_questions)
