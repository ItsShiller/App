class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionMultiple:
    def __init__(self, text, answer, answer_1, answer_2, answer_3):
        self.text = text
        self.answer = answer
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3


class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name
