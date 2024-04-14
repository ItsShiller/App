from tkinter import Button, Canvas
from customtkinter import CTkButton


class Button(Button):
    def __init__(self, text, bg, fg, abg, afg, fn):
        super().__init__()
        self.configure(
            text=text,
            font=("Lalezar", -24),
            borderwidth=0,
            highlightthickness=0,
            bg=bg,
            fg=fg,
            activebackground=abg,
            activeforeground=afg,
            command=fn,
            relief="flat",
            anchor="n",
            justify="center",
        )

    def text_change(self, text):
        self.configure(text=text, font=("Lalezar", -16))

    def get_aswer(self):
        answer = self.get()
        return answer

    def remove(self):
        self.destroy()


class Button_ctk(CTkButton):
    def __init__(self, master, text, bg, fg, w, h, fn):
        super().__init__(master)
        self.configure(
            text=text,
            fg_color=bg,
            text_color=fg,
            hover_color=bg,
            border_width=0,
            font=("Lalezar", 18),
            width=w,
            height=h,
            command=fn,
        )


class Canvas(Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.configure(
            bg="#FFFFFF",
            height=562,
            width=368,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
