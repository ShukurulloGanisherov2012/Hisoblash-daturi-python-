import tkinter.font
from tkinter import *


def salom():
    s1 = entry1.get().title()
    s2 = entry2.get().title()
    a = int(s1)
    b = int(s2)
    c = a + b
    labelNatija['text'] = f"Natija: {c}"


if __name__ == '__main__':
    window = Tk()
    window.geometry("800x600+50+50")
    window.title("2 ta sonni qo'shish dasturi")
    window["bg"] = "#e0a251"

    myfont = tkinter.font.Font(family="Times new roman", size=18, weight="bold")

    label1 = Label(window, text="1-sonni kiriting: ", font=myfont)
    label2 = Label(window, text="2-sonni kiriting: ", font=myfont)
    entry1 = Entry(window, font=myfont)
    entry2 = Entry(window, font=myfont)

    button1 = Button(window, text="Hisobla", command=salom, font=myfont)
    labelNatija = Label(window, text="Natija: ", font=myfont, bg="#e0a251")

    button1.grid(row=2, column=1)
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    labelNatija.grid(row=3, column=1)
    window.mainloop()

