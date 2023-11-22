import re

from enum import Enum


class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple choice"
    SHORT_ANSWER = "short answer"


class QuestionDifficultyLevel(Enum):
    HARD = "hard"
    MEDIUM = "medium"
    EASY = "easy"


QUESTION_TYPE_MAP = {
    "multiple choice": QuestionType.MULTIPLE_CHOICE,
    "short answer": QuestionType.SHORT_ANSWER,
}

QUESTION_DIFFICULTY_LEVEL_MAP = {
    "hard": QuestionDifficultyLevel.HARD,
    "medium": QuestionDifficultyLevel.MEDIUM,
    "easy": QuestionDifficultyLevel.EASY,
}


class Question:
    __type: QuestionType = None
    __statement: str = None
    __answer: str = None
    __difficulty_level: QuestionDifficultyLevel = None
    __subjects: list[str] = None

    def __init__(
        self,
        type: QuestionType,
        statement: str,
        answer: str,
        difficulty_level: QuestionDifficultyLevel,
        subjects: list[str],
    ) -> None:
        self.set_type(type)
        self.set_statement(statement)
        self.set_answer(answer)
        self.set_difficulty_level(difficulty_level)
        self.set_subjects(subjects)

    def set_type(self, type: QuestionType):
        self.__type = type

    def set_statement(self, statement: str):
        self.__statement = statement

    def set_answer(self, answer: str):
        self.__answer = answer

    def set_difficulty_level(self, difficulty_level: QuestionDifficultyLevel):
        self.__difficulty_level = difficulty_level

    def set_subjects(self, subjects: list[str]):
        self.__subjects = subjects

    def get_type(self) -> QuestionType:
        return self.__type

    def get_statement(self) -> str:
        return self.__statement

    def get_answer(self) -> str:
        return self.__answer

    def get_difficulty_level(self) -> QuestionDifficultyLevel:
        return self.__difficulty_level

    def get_subjects(self) -> list[str]:
        return self.__subjects

    def print(self):
        print(f"Type: {self.get_type()}")
        print(f"Statement: {self.get_statement()}")
        print(f"Answer: {self.get_answer()}")
        print(f"Difficulty level: {self.get_difficulty_level()}")
        print(f"Subjects: {self.get_subjects()}")


class QuestionReader:
    def read_question_type(self, question_full_text: str) -> QuestionType:
        regex = r"type = \[.*\];"

        search_result = re.search(regex, question_full_text)

        result = search_result.group()
        result = result.replace("type = ", "")
        result = result.replace("[", "").replace("]", "")
        result = result.replace(";", "")

        return QUESTION_TYPE_MAP[result]

    def read_question_statement(self, question_full_text: str) -> str:
        regex = r"statement = \[.*\];"

        search_result = re.search(regex, question_full_text, flags=re.DOTALL)

        result = search_result.group()
        index_closing_bracket = result.find("];")
        result = result[:index_closing_bracket]

        result = result.replace("statement = ", "")
        result = result.replace("[", "")

        return result

    def read_question_answer(self, question_full_text: str) -> str:
        regex = r"answer = \[.*\];"

        search_result = re.search(regex, question_full_text, flags=re.DOTALL)

        result = search_result.group()
        index_closing_bracket = result.find("];")
        result = result[:index_closing_bracket]

        result = result.replace("answer = ", "")
        result = result.replace("[", "")

        return result

    def read_question_difficulty_level(self, question_full_text: str) -> str:
        regex = r"difficulty_level = \[.*\];"

        search_result = re.search(regex, question_full_text)

        result = search_result.group()
        result = result.replace("difficulty_level = ", "")
        result = result.replace("[", "").replace("]", "")
        result = result.replace(";", "")

        return QUESTION_DIFFICULTY_LEVEL_MAP[result]

    def read_question_subjects(self, question_full_text: str) -> list[str]:
        regex = r"subjects = \[.*\];"

        search_result = re.search(regex, question_full_text)

        result = search_result.group()
        result = result.replace("subjects = ", "")
        result = result.replace("[", "").replace("]", "")
        result = result.split(",")
        result = [r.strip().replace(";", "") for r in result]

        return result

    def read_all_questions(self, file_path: str) -> list[Question]:
        questions = []

        with open(file_path, "rb") as file:
            buffer = file.read().decode()

            question_full_texts = buffer.split(";;")
            question_full_texts = [r for r in question_full_texts if r != ""]

            for question_full_text in question_full_texts:
                type = self.read_question_type(question_full_text)
                statement = self.read_question_statement(question_full_text)
                answer = self.read_question_answer(question_full_text)
                difficulty_level = self.read_question_difficulty_level(
                    question_full_text
                )
                subjects = self.read_question_subjects(question_full_text)

                questions.append(
                    Question(type, statement, answer, difficulty_level, subjects)
                )

        return questions
