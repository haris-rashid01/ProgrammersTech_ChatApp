import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class ChatApp:
    def __init__(self, root, client_socket):
        self.client_socket = client_socket
        self.root = root
        self.root.title("Chat Application")
        self.create_widgets()

        threading.Thread(target=self.receive_messages).start()

    def create_widgets(self):
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(padx=10, pady=5, side=tk.LEFT)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=5, side=tk.RIGHT)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"You: {message}\n")
            self.chat_area.config(state='disabled')

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert(tk.END, f"{message}\n")
                    self.chat_area.config(state='disabled')
            except:
                print("An error occurred. Closing connection.")
                self.client_socket.close()
                break

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_iconbitmap("icon.ico")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))
    app = ChatApp(root, client_socket)
    root.mainloop()
