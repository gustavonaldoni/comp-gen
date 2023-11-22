import os

from question import QuestionReader
from latex import LaTeX
from latexcompiler import LC

FILE_PATH = "./result/exercises.tex"
FULL_FILE_PATH = os.path.abspath(FILE_PATH)


def main():
    question_reader = QuestionReader()
    latex_document = LaTeX()

    latex_document.change_title("Exercises about Computer Science")
    latex_document.change_author("Gustavo Azevedo Naldoni")

    latex_document.document_class()
    latex_document.input("packages.tex")
    latex_document.title()
    latex_document.author()
    latex_document.date()

    latex_document.begin_document()

    latex_document.input("page_style.tex")
    latex_document.make_title()

    questions = question_reader.read_all_questions("./questions_db.txt")

    questions_statements = [q.get_statement() for q in questions]
    questions_answers = [q.get_answer() for q in questions]

    latex_document.section("Exercises")
    latex_document.enumerate(questions_statements)

    latex_document.section("Answers")
    latex_document.enumerate(questions_answers)

    latex_document.end_document()
    latex_document.save_to_file(FILE_PATH)

    print(FULL_FILE_PATH)

    LC.compile_document(
        tex_engine="pdflatex",
        bib_engine="biber",
        no_bib=True,
        path=FULL_FILE_PATH,
        folder_name="./compiled",
    )


if __name__ == "__main__":
    main()
