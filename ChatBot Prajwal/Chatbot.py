# -*- coding: utf-8 -*-
"""
@author: Prajwal
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("FRIDAY")

conversation = [
    "Good morning",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
    "What is your name"
    "My name is FRIDAY"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

from tkinter import *

def ask():
    query=text.get()
    answer=chatbot.get_response(query)
    msg.insert(END, "you :" +query)
    msg.insert(END, "bot :" + str(answer))
    text.delete(0,END)

window = Tk()
window.title("ChatBot")
window.geometry("500x650")

img = PhotoImage(file='image.png')

lbl = Label(window, image=img)
lbl.pack()

frame = Frame(window)

sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
text = Entry(window, font=("Verdana", 16))
text.pack(pady=10)
btn = Button(window, text="Send", command=ask)
btn.pack()
window.mainloop()