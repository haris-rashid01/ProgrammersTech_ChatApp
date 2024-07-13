import tkinter as tk
from tkinter import scrolledtext

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.create_widgets()

    def create_widgets(self):
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(padx=10, pady=5, side=tk.LEFT)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=5, side=tk.RIGHT)

    def send_message(self):
        message = self.message_entry.get()
        self.chat_area.insert(tk.END, f"You: {message}\n")
        self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
