from tkinter import *
import tkinter as tk
import setup_ai as chatbot

root = Tk()
root.title('Chatbot')

text_area = Text(root, width=120, height=50)
text_area.pack()

input_field = Entry(root, width=100)
input_field.pack()

send_button = Button(root, text="Chat!", command=lambda: send_message())
send_button.pack()

def send_message(event) -> None:
    user_input = input_field.get()
    input_field.delete(0, END)

    text_area.insert(END, f"You: {user_input}\n")
    text_area.insert(END, f"\n")
    chatbot.collect_input(user_input)

    response = chatbot.get_completion_from_messages(chatbot.context)
    chatbot.collect_responses(response)

    text_area.insert(END, f"Chatbot: {response}\n")
    text_area.insert(END, f"\n \n")

input_field.bind_all('<Return>', send_message)

root.mainloop()