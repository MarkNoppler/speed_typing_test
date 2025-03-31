"""
What it is:
A speed typing test with a GUI using TkInter to measure words typed per minute

How to use:
Run the programme then type the words on screen as fast as possible.

Documentation:
https://docs.python.org/3/library/tkinter.html
https://www.w3schools.com/python/python_ref_functions.asp

Made by:
Jacob Fairhurst
"""


import tkinter as tk
import random
import time

#sentance list
SENTENCES =  [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Speed typing tests measure your words per minute.",
    "Practice makes perfect when it comes to typing.",
    "Accuracy is just as important as speed in typing."
]


class TypingTest:
    """
    Class for a typing speed test using Tkinter for a GUI.
    WIll display a random sentence for the user to type, calculates typing speed and accuracy.
    """
    def __init__(self, root):
        """Initialise the TKinter window and buttons for the typing test."""
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("600x400")

        self.sentence = random.choice(SENTENCES)
        self.start_time = None

        self.label = tk.Label(root, text=self.sentence, wraplength=500, font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, width=80, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.calculate_speed)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_test, font=("Arial", 12))
        self.restart_button.pack(pady=10)

    def start_timer(self, event):
        """Start the timer when the user begins typing."""
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self, event):
        """Calculates typing speed and accuracy when Enter is pressed. Results will be displayed on screen."""
        if self.start_time is None:
            return

        end_time = time.time()
        elapsed_time = end_time - self.start_time

        typed_text = self.entry.get()
        word_count = len(typed_text.split())

        speed = (word_count / elapsed_time) * 60

        accuracy = sum(1 for a, b in zip(typed_text, self.sentence) if a == b) / max(len(self.sentence), 1) * 100

        self.result_label.config(text=f"Speed: {speed:.2f} WPM | Accuracy: {accuracy:.2f}%")

    def restart_test(self):
        """
        Function to restart the typing speed test with a new random sentence. Clears text field and previous results.
        Focus ensures the user can start typing immediately. Rebinds the timer to each restart.
        """
        self.sentence = random.choice(SENTENCES)
        self.label.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.entry.focus()


#run programme
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()