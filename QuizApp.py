import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.questions = [
            {
                'question': "What is the capital of France?",
                'choices': ["Paris", "Berlin", "London", "Madrid"],
                'correct_choice': 0
            },
            {
                'question': "Which planet is known as the Red Planet?",
                'choices': ["Earth", "Mars", "Venus", "Jupiter"],
                'correct_choice': 1
            },
            {
                'question': "How many continents are there on Earth?",
                'choices': ["4", "6", "7", "5"],
                'correct_choice': 2
            }
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.radio_var, value=i)
            radio.pack()
            self.radio_buttons.append(radio)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

    def next_question(self):
        user_choice = self.radio_var.get()

        if user_choice == -1:
            messagebox.showerror("Error", "Please select an option.")
            return

        if self.questions[self.current_question]['correct_choice'] == user_choice:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()

    def update_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data['question'])

        for i, choice in enumerate(question_data['choices']):
            self.radio_buttons[i].config(text=choice)

        self.radio_var.set(-1)

    def show_result(self):
        messagebox.showinfo("Result", f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    app.update_question()
    root.mainloop()
