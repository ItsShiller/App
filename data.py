import requests
from models import Question, QuestionMultiple, Category


def get_data(category, difficulty, qtype):
    parameters = {
        "amount": 10,
        "category": category,
        "difficulty": difficulty,
        "type": qtype,
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)

    question_data = response.json()
    questions = []

    for question in question_data["results"]:
        questions.append(Question(question["question"], question["correct_answer"]))
    return questions


def get_data_multiple(category, difficulty, qtype):
    parameters = {
        "amount": 10,
        "category": category,
        "difficulty": difficulty,
        "type": qtype,
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)

    question_data = response.json()
    questions = []

    for question in question_data["results"]:
        questions.append(
            QuestionMultiple(
                question["question"],
                question["correct_answer"],
                question["incorrect_answers"][0],
                question["incorrect_answers"][1],
                question["incorrect_answers"][2],
            )
        )
    return questions


def category_list():
    response = requests.get(url="https://opentdb.com/api_category.php")
    category_data = response.json()
    categories = []
    for category in category_data["trivia_categories"]:
        categories.append(Category(category["id"], category["name"]))
    return categories
