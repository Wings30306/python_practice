def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")

    option = input("Enter option: ")
    return option


def ask_questions():
    questions = []
    answers = []

    with open("quiz/questions.txt", "r") as file:
        lines = file.read().splitlines()

    for i, text in enumerate(lines):
        if i % 2 == 0:
            questions.append(text)
        else:
            answers.append(text)

    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)

    score = 0

    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess.lower() == answer.lower():
            score += 1
            print("Correct!")
            print(score)
        else:
            print("Wrong!")

    print("You got {0} correct out of {1}.".format(score, number_of_questions))


def add_question():
    print("")
    question = input("Enter a question\n> ")

    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))

    print("Your question: {0} \nAnswer: {1}".format(question.capitalize(), answer.capitalize()))
    check = input("Please confirm that this question and answer are correct: y/n \n> ")
    for check in check:
        if check.lower() == "y":
           file = open("quiz/questions.txt", "a")
           file.write(question.capitalize() + "\n")
           file.write(answer.capitalize() + "\n")
           file.close()
        elif check.lower() == "n":
            print("Your question has been deleted.")
            break
        else:
            print("Invalid option, please try again.")
        print("")


def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")


game_loop()
