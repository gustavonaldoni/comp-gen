import re
from question.question import (
    Question,
    QuestionType,
    QUESTION_TYPE_MAP,
    QUESTION_DIFFICULTY_LEVEL_MAP,
)
from question.filter import Filter, FilterOperation


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
        result = result.replace("[", "").replace("]", "")
        result = re.sub(r"answer = .*", "", result)

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

    def read_all_questions_with_filter(
        self, file_path: str, filter: Filter
    ) -> list[Question]:
        filtered_questions = []
        all_questions = self.read_all_questions(file_path)

        print("================================")

        if filter.operation == FilterOperation.AND:
            for question in all_questions:
                needed_score = 3
                score = 0

                if len(filter.types) == 0:
                    needed_score -= 1
                else:
                    if question.get_type() in filter.types:
                        score += 1
                        print("Increasing score by type ...")

                if len(filter.difficulty_levels) == 0:
                    needed_score -= 1
                else:
                    if question.get_difficulty_level() in filter.difficulty_levels:
                        score += 1
                        print("Increasing score by difficulty level ...")

                if len(filter.subjects) == 0:
                    needed_score -= 1
                else:
                    for subject in filter.subjects:
                        if subject in question.get_subjects():
                            score += 1
                            print("Increasing score by subject ...")

                print()

                question.print()
                print()
                print(f"Final score = {score}")
                print("================================")

                if score >= needed_score:
                    filtered_questions.append(question)

        elif filter.operation == FilterOperation.OR:
            for question in all_questions:
                if question.get_type() in filter.types:
                    filtered_questions.append(question)
                    continue

                if question.get_difficulty_level() in filter.difficulty_levels:
                    filtered_questions.append(question)
                    continue

                for subject in filter.subjects:
                    if subject in question.get_subjects():
                        filtered_questions.append(question)
                        continue

        else:
            raise ValueError("Invalid operation!")

        return filtered_questions
