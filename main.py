from question import Question, QuestionReader

def main():
    question_reader = QuestionReader()
    question_reader.read_all_questions('./questions_db.txt')

if __name__ == '__main__':
    main()