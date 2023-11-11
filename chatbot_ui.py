from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
import setup_ai as chatbot

def send_message():
    user_message = message_input.get("1.0", tk.END).strip()
    if user_message:
        # Nachricht zur Historie hinzufügen
        add_message("Benutzer", user_message)

        # Hier würden wir später die Nachricht an das Language Model senden
        # und die Antwort hinzufügen
        # Zum Testen fügen wir einfach eine Echo-Antwort hinzu
        add_message("Bot", "Echo: " + user_message)

    # Eingabefeld leeren
    message_input.delete("1.0", tk.END)

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

window = Tk()
window.title('Chatbot')

# Nachrichtenverlauf
message_history = scrolledtext.ScrolledText(window, state='disabled', wrap='word')
message_history.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Nachrichteneingabe
message_input = tk.Text(window, height=3)
message_input.grid(row=1, column=0, sticky='nsew')

# Senden-Button
send_button = tk.Button(window, text="Senden", command=send_message)
send_button.grid(row=1, column=1, sticky='nsew')

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