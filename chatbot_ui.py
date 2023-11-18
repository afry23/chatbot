from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinterweb import HtmlFrame
from dotenv import load_dotenv
from tkinter import PhotoImage
import setup_ai as chatbot
import chatbot_css as html_info

load_dotenv()

# Globale Variable für den Standard-Prompt
default_prompt = "You are a helpful assistant."


def send_message():
    default_prompt = default_prompt_input.get("1.0", tk.END).strip()
    if chatbot.context == []:
        chatbot.add_prompt(default_prompt)
    user_message = message_input.get("1.0", tk.END).strip()
    if user_message:
        # Nachricht zur Historie hinzufügen
        add_message("user", user_message)
        get_response(user_message)
    # Eingabefeld leeren
    message_input.delete("1.0", tk.END)

def get_response(message):
    add_message("bot", f'Echo: {message}')
    # try:
    #     # Anfrage an das ausgewählte Language Model senden
    #     selected_model = model_selector.get()
    #     if selected_model in [chatbot.LanguageModel.DAVINCI.value, chatbot.LanguageModel.CURIE.value]:
    #         response = chatbot.get_completion(message, selected_model)
    #     else:
    #         response = chatbot.get_chat_completion_from_messages(chatbot.context, selected_model)
    #     bot_message = response.strip()
    #     add_message("bot", bot_message)
    # except Exception as e:
    #     add_message("bot", f"Fehler bei der Kommunikation mit OpenAI: {e}")

def add_message(sender, message):
    global html_content
    new_message = f"<div class='message {sender}'>{message}</div>"
    html_content = html_content.replace("<!-- Messages go here -->", f"{new_message}<!-- Messages go here -->")
    # Nachrichtenformatierung
    if sender == "user":
        chatbot.collect_input(message)
    else:
        chatbot.collect_responses(message)

    # Nachricht zur Historie hinzufügen
    message_history.html_content += new_message
    message_history.load_html(message_history.html_content)

def start_speech_recognition():
    # Hier kommt die Logik für die Spracheingabe
    pass

# HTML-Struktur
html_content = f"""
<html>
<head>
    <style>
    {html_info.css}
    </style>
</head>
<body>
    <div class='container'>
        <!-- Messages go here -->
    </div>
</body>
</html>
"""

window = Tk()
window.title('Chatbot')

# Icons laden
send_icon = PhotoImage(file='send.png')
speech_icon = PhotoImage(file='microphone.png')

# Model-Auswahl
model_selector = ttk.Combobox(window, values=[model.value for model in chatbot.LanguageModel])
model_selector.grid(row=0, column=0, padx=5, pady=2.5, sticky='nsew')
model_selector.set(chatbot.LanguageModel.GPT3_TURBO.value) # Standardmodell

# Standard-Prompt Eingabefeld
default_prompt_input = scrolledtext.ScrolledText(window, height=3)
default_prompt_input.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=5, pady=2.5)
default_prompt_input.insert("1.0", default_prompt)

# Nachrichtenverlauf
message_history = HtmlFrame(window, horizontal_scrollbar="auto")
message_history.html_content = html_info.html_content #"<style> .user {color: blue;} .bot {color: green;} </style>"
message_history.grid(row=2, column=0, columnspan=3, sticky='nsew', padx=5, pady=2.5)

# Nachrichteneingabe
message_input = tk.Text(window, height=3)
message_input.grid(row=3, column=0, sticky='nsew', padx=5, pady=2.5)

# Senden-Button
send_button = tk.Button(window, image=send_icon, width=30, command=send_message)
send_button.grid(row=3, column=1, sticky='nsew', padx=5, pady=2.5)

# Spracheingabe-Button
speech_button = tk.Button(window, image=speech_icon, width=30, command=start_speech_recognition)
speech_button.grid(row=3, column=2, sticky='nsew', padx=5, pady=2.5)

# Fenstergröße und Layout
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)

window.mainloop()