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
import time
import random
from typing import Optional


SENTENCES: list[str] = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests are a great way to improve accuracy.",
    "Practice makes perfect when learning to type fast."
]


class TypingTest:
    """
    A typing speed test using Tkinter for a GUI.
    Displays a random sentence for the user to type and calculates typing speed and accuracy.
    """

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the Tkinter window and UI components for the typing test."""
        self.root: tk.Tk = root
        self.root.title("Speed Typing Test")
        self.root.geometry("600x400")

        self.sentence: str = random.choice(SENTENCES)
        self.start_time: Optional[float] = None

        self.label: tk.Label = tk.Label(root, text=self.sentence, wraplength=500, font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry: tk.Entry = tk.Entry(root, width=80, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.calculate_speed)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result_label: tk.Label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.restart_button: tk.Button = tk.Button(root, text="Restart", command=self.restart_test, font=("Arial", 12))
        self.restart_button.pack(pady=10)


    def start_timer(self, event: tk.Event) -> None:
        """Start the timer when the user begins typing."""
        if self.start_time is None:
            self.start_time = time.time()


    def calculate_speed(self, event: tk.Event) -> None:
        """
        Calculate typing speed (words per minute) and accuracy when Enter is pressed.
        Display results on the screen.
        """
        if self.start_time is None:
            return

        end_time: float = time.time()
        elapsed_time: float = end_time - self.start_time

        typed_text: str = self.entry.get()
        word_count: int = len(typed_text.split())

        speed: float = (word_count / elapsed_time) * 60

        accuracy: float = sum(1 for a, b in zip(typed_text, self.sentence) if a == b) / max(len(self.sentence), 1) * 100

        self.result_label.config(text=f"Speed: {speed:.2f} WPM | Accuracy: {accuracy:.2f}%")


    def restart_test(self) -> None:
        """
        Restart the typing speed test with a new random sentence.
        Clears the text field and previous results. Ensures focus is on the entry field.
        """
        self.sentence = random.choice(SENTENCES)
        self.label.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
