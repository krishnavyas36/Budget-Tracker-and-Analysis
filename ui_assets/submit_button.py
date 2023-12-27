from tkinter import *

class SubmitButton:
    def __init__(self, frame, fill_type):
        self.f = frame
        self.f.propagate(0)
        self.f.pack()

        self.submitButton = Button(self.f,width=15,height=1,bg="#a04",font=('Helvetica',-25),text="Add Transaction", command=lambda: self.submitted())
        self.submitButton.pack(fill=fill_type, side=BOTTOM)

    def submitted(self):
        print("Transaction Added")

if __name__ == "__main__":
    root = Tk()
    f = Frame(root,width=1000,height=600,bg='#0E2954')  
    mainSubmit = SubmitButton(f, X)
    root.title("Budget Tracker")
    root.mainloop()
