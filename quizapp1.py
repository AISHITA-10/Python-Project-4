import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

questions = [
    {"question": "Q1. What keyword is used to create a function in Python?", "options": ["def", "function", "func", "define"], "answer": "def"},
    {"question": "Q2. Which of the following is a mutable data type in Python?", "options": ["list", "tuple", "string", "integer"], "answer": "list"},
    {"question": "Q3. What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "12"], "answer": "8"},
    {"question": "Q4. Which of the following is a Python framework for web development?", "options": ["Django", "Numpy", "Pandas", "Scikit-learn"], "answer": "Django"},
    {"question": "Q5. How do you start a comment in Python?", "options": ["//", "/*", "#", "<!--"], "answer": "#"},
    {"question": "Q6. Which method is used to add an element at the end of a list?", "options": ["append()", "add()", "insert()", "extend()"], "answer": "append()"},
    {"question": "Q7. What does 'PEP' stand for in Python?", "options": ["Python Enhancement Proposal", "Python Enhanced Performance", "Python Efficient Programming", "Python Enterprise Project"], "answer": "Python Enhancement Proposal"},
    {"question": "Q8. What is the result of the expression '3' + '3'?", "options": ["6", "33", "9", "Error"], "answer": "33"},
    {"question": "Q9. Which built-in function is used to get the length of a list?", "options": ["len()", "length()", "count()", "size()"], "answer": "len()"},
    {"question": "Q10. Which of the following is a built-in data type in Python?", "options": ["set", "map", "filter", "reduce"], "answer": "set"}
]

class QuizApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("600x400")
        self.score = 0
        self.current_question = 0
        self.create_background()
        self.create_widgets()
    
    def create_background(self):
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = ImageTk.PhotoImage(Image.open("quiz.jpg"))
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to the Python Quiz", font=("Helvetica", 24, "bold"), bg="lightblue")
        self.title_window = self.canvas.create_window(100, 20, anchor="nw", window=self.title_label)
        
        self.question_label = tk.Label(self.root, text=questions[self.current_question]["question"], font=("Helvetica", 16), bg="white")
        self.question_window = self.canvas.create_window(50, 100, anchor="nw", window=self.question_label)
        
        self.options = tk.StringVar(value="")
        self.options_frame = tk.Frame(self.root, bg="white")
        self.options_window = self.canvas.create_window(50, 150, anchor="nw", window=self.options_frame)
        
        for option in questions[self.current_question]["options"]:
            tk.Radiobutton(self.options_frame, text=option, variable=self.options, value=option, font=("Helvetica", 14), bg="white").pack(anchor="w")
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Helvetica", 14), bg="green", fg="white")
        self.submit_window = self.canvas.create_window(250, 300, anchor="nw", window=self.submit_button)
    
    def check_answer(self):
        if self.options.get() == questions[self.current_question]["answer"]:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question == len(questions):
            messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}")
            self.root.quit()
        else:
            self.update_question()
    
    def update_question(self):
        self.question_label.config(text=questions[self.current_question]["question"])
        
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        for option in questions[self.current_question]["options"]:
            tk.Radiobutton(self.options_frame, text=option, variable=self.options, value=option, font=("Helvetica", 14), bg="white").pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApplication(root)
    root.mainloop()
