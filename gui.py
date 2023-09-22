import tkinter as tk
from tkinter import ttk


class Mailer_GUI(object):
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Sender")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        # From
        self.left_margin = ttk.Label(master=self.root, text="                         ")
        self.left_margin.grid(row=0, column=0)
        self.from_label = ttk.Label(master=self.root, text="From: ", font="calibre 12 bold")
        self.from_label.grid(row=0, column=1)
        self.from_input = tk.StringVar()
        self.from_field = tk.Entry(master=self.root, textvariable=self.from_input, width=60)
        self.from_field.grid(row=0, column=2, pady=10)
        # To
        self.left_margin.grid(row=1, column=0)
        self.to_label = ttk.Label(master=self.root, text="To: ", font="calibre 12 bold")
        self.to_label.grid(row=1, column=1)
        self.to_input = tk.StringVar()
        self.to_field = tk.Entry(master=self.root, textvariable=self.to_input, width=60)
        self.to_field.grid(row=1, column=2)
        # Or
        self.or_label = ttk.Label(master=self.root, text="OR", font="calibre 8 bold")
        self.or_label.grid(row=2, column=2)
        # Button
        self.file_button = ttk.Button(master=self.root, text="SELECT FILE")
        self.file_button.grid(row=3, column=2)
        # Subject
        self.left_margin.grid(row=4, column=0)
        self.subject_label = ttk.Label(master=self.root, text="Subject: ", font="calibre 12 bold")
        self.subject_label.grid(row=4, column=1)
        self.subject_input = tk.StringVar()
        self.subject_field = tk.Entry(master=self.root, textvariable=self.subject_input, width=60)
        self.subject_field.grid(row=4, column=2)
        # Body
        self.body_input = tk.StringVar()
        self.body_field = tk.Text(master=self.root, width=45, height=20)
        self.body_field.grid(row=5, column=2, pady=10)
        # Send Button
        self.send_button = ttk.Button(master=self.root, text="SEND")
        self.send_button.grid(row=6, column=2)


if __name__ == "__main__":
    window = tk.Tk()
    post_master = Mailer_GUI(window)
    window.mainloop()
