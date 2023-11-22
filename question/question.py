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
