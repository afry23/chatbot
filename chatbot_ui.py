from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from dotenv import load_dotenv
from enum import Enum

import openai
import setup_ai as chatbot

load_dotenv()

# Globale Variable für den Standard-Prompt
default_prompt = ""
class LanguageModel(Enum):
    GPT4_TURBO = "gpt-4-1106-preview"
    GPT4 = "gpt-4"
    GPT3_TURBO = "gpt-3.5-turbo"
    DAVINCI = "text-davinci-003"
    CURIE = "text-curie-001"

def send_message():
    user_message = message_input.get("1.0", tk.END).strip()
    if user_message:
        # Nachricht zur Historie hinzufügen
        add_message("Benutzer", user_message)
        get_response(user_message)
    # Eingabefeld leeren
    message_input.delete("1.0", tk.END)

def get_response(message):
    try:
        # Anfrage an das ausgewählte Language Model senden
        selected_model = model_selector.get()
        if selected_model in [LanguageModel.DAVINCI.value, LanguageModel.CURIE.value]:
            response = openai.Completion.create(
                engine=selected_model,
                prompt=message,
                max_tokens=150
            )
        else:
            response = openai.ChatCompletion.create(
                model=selected_model,
                prompt=message,
                temperature=0,
            )
            pass
        bot_message = response.choices[0].text.strip()
        add_message("Bot", bot_message)
    except Exception as e:
        add_message("Bot", f"Fehler bei der Kommunikation mit OpenAI: {e}")

def add_message(sender, message):
    # Nachrichtenformatierung
    if sender == "Benutzer":
        formatted_message = f"**{sender}**: {message}\n\n"
    else:
        formatted_message = f"    **{sender}**: {message}\n\n"

    # Nachricht zur Historie hinzufügen
    message_history.configure(state='normal')
    message_history.insert(tk.END, formatted_message)
    message_history.configure(state='disabled')

    # Automatisches Scrollen
    message_history.see(tk.END)

def start_speech_recognition():
    # Hier kommt die Logik für die Spracheingabe
    pass

window = Tk()
window.title('Chatbot')

# Model-Auswahl
model_selector = ttk.Combobox(window, values=[model.value for model in LanguageModel])
model_selector.grid(row=0, column=0, sticky='nsew')
model_selector.set(LanguageModel.DAVINCI.value) # Standardmodell

# Standard-Prompt Eingabefeld
default_prompt_input = scrolledtext.ScrolledText(window, height=3)
default_prompt_input.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)

# Nachrichtenverlauf
message_history = scrolledtext.ScrolledText(window, state='disabled', wrap='word')
message_history.grid(row=2, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)

# Nachrichteneingabe
message_input = tk.Text(window, height=3)
message_input.grid(row=3, column=0, sticky='nsew')

# Senden-Button
send_button = tk.Button(window, text="Senden", command=send_message)
send_button.grid(row=3, column=1, sticky='nsew')

# Spracheingabe-Button
speech_button = tk.Button(window, text="Spracheingabe", command=start_speech_recognition)
speech_button.grid(row=3, column=2, sticky='nsew')

# Fenstergröße und Layout
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)

# text_area = Text(window, width=120, height=50)
# text_area.pack()

# input_field = Entry(window, width=100)
# input_field.pack()

# send_button = Button(window, text="Chat!", command=lambda: send_message())
# send_button.pack()

# def send_message(event) -> None:
#     user_input = input_field.get()
#     input_field.delete(0, END)

#     text_area.insert(END, f"You: {user_input}\n")
#     text_area.insert(END, f"\n")
#     chatbot.collect_input(user_input)

#     response = chatbot.get_completion_from_messages(chatbot.context)
#     chatbot.collect_responses(response)

#     text_area.insert(END, f"Chatbot: {response}\n")
#     text_area.insert(END, f"\n \n")

# input_field.bind_all('<Return>', send_message)

window.mainloop()