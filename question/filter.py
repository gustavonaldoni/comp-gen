from dataclasses import dataclass
from enum import Enum

from question.question import QuestionType, QuestionDifficultyLevel


class FilterOperation(Enum):
    AND = "and"
    OR = "or"


@dataclass
class Filter:
    types: list[QuestionType]
    difficulty_levels: list[QuestionDifficultyLevel]
    subjects: list[str]
    operation: FilterOperation
    number_of_questions: int
    is_random: bool
