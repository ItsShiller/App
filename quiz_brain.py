import html
import random


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def still_has_questions_click(self):
        return self.question_number <= len(self.question_list)

    def next_question(self):
        # answer = input(
        #     f"Q.{self.question_number + 1}: {html.unescape(self.question_list[self.question_number].text)} (True/False)?: "
        # )
        if self.still_has_questions():
            question = f"Q.{self.question_number + 1}: {html.unescape(self.question_list[self.question_number].text)}"
        else:
            question = "That was the last question."
        self.question_number += 1
        # self.check_answer(answer, self.question_list[self.question_number - 1].answer)
        return question

    def next_answer(self):

        self.question_number -= 1
        answer_list = []
        answer_list.append(
            html.unescape(self.question_list[self.question_number].answer)
        )
        answer_list.append(
            html.unescape(self.question_list[self.question_number].answer_1)
        )
        answer_list.append(
            html.unescape(self.question_list[self.question_number].answer_2)
        )
        answer_list.append(
            html.unescape(self.question_list[self.question_number].answer_3)
        )
        random.shuffle(answer_list)
        self.question_number += 1
        return answer_list

    def check_answer(self, user_answer):
        if (
            user_answer.lower()
            == self.question_list[self.question_number - 1].answer.lower()
        ):
            print("You got it right!")
            self.score += 1
            return True
        else:
            print("Thats wrong.")
            print(
                f"The correct answer was {self.question_list[self.question_number - 1].answer.lower()}."
            )
            if self.question_number < len(self.question_list):
                print(f"Your current score is: {self.score}/{self.question_number}")
            return False
