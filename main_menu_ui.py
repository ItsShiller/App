from tkinter import Tk, Entry, Text, PhotoImage, messagebox
from customtkinter import *
from data import *
from ui_elements import Button, Canvas
from quiz_brain import QuizBrain
from data import *
import pyglet
import random

pyglet.options["win32_gdi_font"] = True
pyglet.font.add_file("./assets/Lalezar.ttf")
FONT = ("Lalezar", -24)

difficulty = ""
game_mode = ""
category = ""
game_start = False
question = ""
score = 0
tester = -1
user_answer = ""
list = category_list()
options = ["Random Mix"]
options_id = [""]
answer_list = []
for i in range(0, len(list)):
    options.append(list[i].name)
for i in range(0, len(list)):
    options_id.append(list[i].id)


# Button Functionality


# Main menu buttons
def menu_button_fn():
    window.destroy()


def tf_button_fn():
    global game_mode
    game_mode = "boolean"
    tf_button.configure(background="#00B0F0")
    choice_button.configure(background="Grey")


def start_button_fn():
    global category, game_start, options, options_id, quiz_brain, question_bank
    for i in range(0, len(list)):
        if category_choice.get() == options[i]:
            category = options_id[i]
    if game_mode == "boolean":
        question_bank = get_data(category, difficulty, game_mode)
    if game_mode == "multiple":
        question_bank = get_data_multiple(category, difficulty, game_mode)
    quiz_brain = QuizBrain(question_bank)
    canvas.destroy()
    if game_mode == "boolean":
        true_false()
    elif game_mode == "multiple":
        pick_answer()
    else:
        main_menu()


def choice_button_fn():
    global game_mode
    game_mode = "multiple"
    tf_button.configure(background="Grey")
    choice_button.configure(background="#00B0F0")


def easy_button_fn():
    global difficulty
    difficulty = "easy"
    hard_button.configure(background="Grey")
    medium_button.configure(background="Grey")
    easy_button.configure(background="#66FF99")


def medium_button_fn():
    global difficulty
    difficulty = "medium"
    hard_button.configure(background="Grey")
    medium_button.configure(background="#FFC000")
    easy_button.configure(background="Grey")


def hard_button_fn():
    global difficulty
    difficulty = "hard"
    hard_button.configure(background="#FF66FF")
    medium_button.configure(background="Grey")
    easy_button.configure(background="Grey")


# Boolean game mode buttons
def true_button_fn():
    global user_answer
    user_answer = "true"
    test_answer()


def false_button_fn():
    global user_answer
    user_answer = "false"
    test_answer()


# Multiple choice mode
def button_a_fn():
    global user_answer
    user_answer = answer_list[0]
    test_answer()


def button_b_fn():
    global user_answer
    user_answer = answer_list[1]
    test_answer()


def button_c_fn():
    global user_answer
    user_answer = answer_list[2]
    test_answer()


def button_d_fn():
    global user_answer
    user_answer = answer_list[3]
    test_answer()


# Question functions
def test_answer():
    global score, tester
    tester += 1
    if tester < len(question_bank):
        quiz_brain.check_answer(user_answer)
        if quiz_brain.check_answer(user_answer):
            if game_mode == "multiple":
                canvas.coords(question_txt, 90, 124)
            else:
                canvas.coords(question_txt, 90, 180)
            canvas.itemconfig(
                question_txt,
                text="CORRECT ANSWER!",
                fill="#66FF99",
                font=("Lalezar", 50 * -1),
            )
            score += 1
        else:
            if game_mode == "multiple":
                canvas.coords(question_txt, 90, 124)
            else:
                canvas.coords(question_txt, 90, 180)
            canvas.itemconfig(
                question_txt,
                text="WRONG ANSWER!",
                justify="center",
                fill="#FF4E89",
                font=("Lalezar", 50 * -1),
            )
        canvas.itemconfig(score_txt, text=f"SCORE: {score}")
        canvas.after(1000, get_next_question)


def get_next_question():
    global question, answer_list, button_a
    if quiz_brain.still_has_questions():
        if game_mode == "multiple":
            canvas.coords(question_txt, 25, 137)
        else:
            canvas.coords(question_txt, 27, 165)
        question = quiz_brain.next_question()
        canvas.itemconfig(
            question_txt, text=question, fill="#000000", font=("Lalezar", 20 * -1)
        )
        if game_mode == "multiple":
            answer_list = quiz_brain.next_answer()
            button_a.text_change(answer_list[0])
            button_b.text_change(answer_list[1])
            button_c.text_change(answer_list[2])
            button_d.text_change(answer_list[3])
    else:
        canvas.coords(question_txt, 45, 190)
        canvas.itemconfig(
            question_txt,
            text=f"Final score: {score}",
            fill="#000000",
            font=("Lalezar", 50 * -1),
        )
        #
        # Restart function WIP, buttons in game mode not working afteer restart, while Main Menu is fully functional
        #
        if game_mode == "multiple":
            button_a.place_forget()
            button_b.place_forget()
            button_c.place_forget()
            button_d.place_forget()
            menu_button = Button(
                "EXIT",
                "#00B0F0",
                "White",
                "#00B0F0",
                "Black",
                menu_button_fn,
            )
            menu_button.place(x=30.0, y=455.0, width=308.0, height=34.0)
        if game_mode == "boolean":
            button_1.place_forget()
            button_2.place_forget()
            menu_button = Button(
                "EXIT",
                "#00B0F0",
                "White",
                "#00B0F0",
                "Black",
                menu_button_fn,
            )
            menu_button.place(x=30.0, y=455.0, width=308.0, height=34.0)


# UI START
window = Tk()

window.geometry("368x562")
window.configure(bg="#FFFFFF")


# Main Menu
def main_menu():
    global easy_button, medium_button, hard_button, tf_button, choice_button, category_choice, window, canvas, options_id, options, list

    canvas = Canvas(window)
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=("./assets/frame0/image_1.png"))
    image_1 = canvas.create_image(184.0, 281.0, image=image_image_1)

    image_image_2 = PhotoImage(file=("./assets/frame0/image_2.png"))
    image_2 = canvas.create_image(189.0, 129.0, image=image_image_2)

    image_image_3 = PhotoImage(file=("./assets/frame0/image_3_2.png"))
    image_3 = canvas.create_image(184.0, 332.0, image=image_image_3)

    image_image_4 = PhotoImage(file=("./assets/frame0/image_4.png"))
    image_4 = canvas.create_image(184.0, 413.0, image=image_image_4)

    image_image_5 = PhotoImage(file=("./assets/frame0/image_5.png"))
    image_5 = canvas.create_image(184.0, 251.0, image=image_image_5)

    start_button = Button(
        "Start",
        "#00B0F0",
        "White",
        "#00B0F0",
        "Black",
        start_button_fn,
    )
    start_button.place(x=30.0, y=487.0, width=308.0, height=34.0)

    hard_button = Button("Hard", "#FF66FF", "White", "#FF66FF", "Black", hard_button_fn)
    hard_button.place(x=246.0, y=432.0, width=92.0, height=34.0)

    medium_button = Button(
        "Medium", "#FFC000", "White", "#FFC000", "Black", medium_button_fn
    )
    medium_button.place(x=138.0, y=432.0, width=92.0, height=34.0)

    easy_button = Button("Easy", "#66FF99", "White", "#66FF99", "Black", easy_button_fn)
    easy_button.place(x=30.0, y=432.0, width=92.0, height=34.0)

    choice_button = Button(
        "Pick Answer", "#00B0F0", "White", "#00B0F0", "Black", choice_button_fn
    )
    choice_button.place(x=192.0, y=351.0, width=146.0, height=34.0)

    tf_button = Button(
        "True/False",
        "#00B0F0",
        "White",
        "#00B0F0",
        "Black",
        tf_button_fn,
    )
    tf_button.place(x=30.0, y=351.0, width=146.0, height=34.0)

    category_choice = CTkComboBox(canvas, values=options, width=308.0, height=34.0)
    category_choice.configure(
        fg_color="#00B0F0",
        bg_color="#00B0F0",
        border_width=0,
        button_color="#00B0F0",
        button_hover_color="#00B0F0",
        justify="center",
        font=("Lalezar", -20),
        dropdown_font=("Lalezar", -16),
    )
    category_choice.place(
        x=30.0,
        y=270.0,
    )

    window.resizable(False, False)
    canvas.mainloop()


# Game in True/False mode
def true_false():
    global question_txt, canvas, score_txt, button_1, button_2

    canvas = Canvas(window)

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=("./assets/frame0/image_1.png"))
    image_1 = canvas.create_image(184.0, 281.0, image=image_image_1)

    score_txt = canvas.create_text(
        105.0,
        15.0,
        anchor="nw",
        text=f"SCORE: {score}",
        fill="#FFFFFF",
        font=("Lalezar", 36 * -1),
    )

    button_1 = Button("False", "#FF5991", "White", "#FF5991", "Black", false_button_fn)
    button_1.place(x=192.0, y=458.0, width=146.0, height=34.0)

    button_2 = Button("True", "#66FF99", "White", "#66FF99", "Black", true_button_fn)
    button_2.place(x=30.0, y=458.0, width=146.0, height=34.0)

    image_image_2 = PhotoImage(file=("./assets/frame0/image_2_frame1.png"))
    image_2 = canvas.create_image(183.0, 262.0, image=image_image_2)

    question_txt = canvas.create_text(
        8.0,
        124.0,
        width=340,
        anchor="nw",
        text=question,
        fill="#000000",
        font=("Lalezar", 20 * -1),
        justify="center",
    )
    get_next_question()
    window.resizable(False, False)
    canvas.mainloop()


# Game in multiple answer mode
def pick_answer():
    global canvas, score, question_txt, score_txt, button_a, button_b, button_c, button_d

    canvas = Canvas(window)
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=("./assets/frame0/image_1.png"))
    image_1 = canvas.create_image(184.0, 281.0, image=image_image_1)
    image_image_2 = PhotoImage(file=("./assets/frame0/image_2_frame1.png"))
    image_2 = canvas.create_image(184.0, 200.0, image=image_image_2)

    score_txt = canvas.create_text(
        105.0,
        15.0,
        anchor="nw",
        text=f"SCORE: {score}",
        fill="#FFFFFF",
        font=("Lalezar", 36 * -1),
    )

    question_txt = canvas.create_text(
        8.0,
        124.0,
        width=340,
        anchor="nw",
        text=question,
        fill="#000000",
        font=("Lalezar", 20 * -1),
        justify="center",
    )

    button_a = Button("False", "#00B0F0", "Black", "#00B0F0", "Black", button_a_fn)
    button_a.place(x=31.0, y=354.0, width=300.0, height=34.0)

    button_b = Button("False", "#FEF200", "Black", "#FEF200", "Black", button_b_fn)
    button_b.place(x=31.0, y=405.0, width=300.0, height=34.0)

    button_c = Button("False", "#8ED9F9", "Black", "#8ED9F9", "Black", button_c_fn)
    button_c.place(x=31.0, y=456.0, width=300.0, height=34.0)

    button_d = Button("False", "#FF66FF", "Black", "#FF66FF", "Black", button_d_fn)
    button_d.place(x=31.0, y=507.0, width=300.0, height=34.0)

    get_next_question()
    window.resizable(False, False)
    canvas.mainloop()


main_menu()
