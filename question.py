import re

from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE = 'multiple choice'
    SHORT_ANSWER = 'short answer'

class QuestionDifficultyLevel(Enum):
    HARD = 'hard'
    MEDIUM = 'medium'
    EASY = 'easy'

class QuestionSubjects(Enum):
    CALCULUS = 'calculus'
    LINEAR_ALGEBRA = 'linear algebra'
    NUMBER_THEORY = 'number theory'
    DISCRETE_MATH = 'discrete math'
    GRAPH_THEORY = 'graph theory'
    GAME_THEORY = 'game theory'
    MATHEMATICAL_LOGIC = 'mathematical logic'

    ALGORITHMS = 'algorithms'
    DATA_STRUCTURES = 'data structures'

    COMPUTER_ARCHITECTURE = 'computer architecture'
    OPERATING_SYSTEMS = 'operating systems'

    AUTOMATA_THEORY = 'automata theory'
    COMPUTABILITY_THEORY = 'computability theory'
    COMPLEXITY_THEORY = 'complexity theory'

    COMPILERS = 'compilers'
    PROGRAMMING_LANGUAGE_PRAGMATICS = 'programming language pragmatics'
    PROGRAMMING_LANGUAGE_THEORY = 'programming language theory'
    TYPE_THEORY = 'type theory'

    ROBOTICS = 'robotics'

    RELATIONAL_DATABASES = 'relational databases'
    STRUCTURED_STORAGE = 'structures storage'

    PARALLEL_COMPUTING = 'parallel computing'
    CONCURRENCY = 'concurrency'
    DISTRIBUTED_COMPUTING = 'distributed computing'

class Question:
    __type: QuestionType = None
    __statement: str = None
    __answer: str  = None
    __difficulty_level: QuestionDifficultyLevel = None
    __subjects: list[QuestionSubjects] = None

    def set_type(self, type: QuestionType):
        self.__type = type

    def set_statement(self, statement: str):
        self.__statement = statement

    def set_answer(self, answer: str):
        self.__answer = answer
    
    def set_difficulty_level(self, difficulty_level: QuestionDifficultyLevel):
        self.__difficulty_level = difficulty_level
        
    def set_subjects(self, subjects: list[QuestionSubjects]):
        self.__subjects = subjects

    def get_type(self) -> QuestionType:
        return self.__type

    def get_statement(self) -> str:
        return self.__statement

    def get_answer(self) -> str:
        return self.__answer
    
    def get_difficulty_level(self) -> QuestionDifficultyLevel:
        return self.__difficulty_level
    
    def get_subjects(self) -> list[QuestionSubjects]:
        return self.__subjects

class QuestionReader:
    def read_all_questions(self, file_path: str) -> list[Question]:
        questions = []

        with open(file_path, 'rb') as file:
            buffer = file.read().decode()

            regex = r'\[.*\]'

            questions = re.findall(regex, buffer)

            print(buffer)
            print(questions)
