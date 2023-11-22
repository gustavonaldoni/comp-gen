from question import QuestionReader


def main():
    question_reader = QuestionReader()
    questions = question_reader.read_all_questions("./questions_db.txt")

    for question in questions:
        question.print()
        print()

if __name__ == "__main__":
    main()
