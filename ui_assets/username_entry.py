from tkinter import *

class UserNameEntry:
    def __init__(self, frame, label_name, label_x, label_y, entry_x, entry_y):
        self.f = frame
        self.f.propagate(0)
        self.f.pack()

        self.l1 = Label(self.f,text="Enter "+label_name,font=('Helvetica',-20))
# , bg='#151617'
        
        self.var = StringVar()
        self.e1 = Entry(self.f,width=50, fg='black',bg='#FDF7E4',font=('Arial',14), textvariable=self.var,bd=4, relief="groove", insertbackground="black")

        
        self.l1.place(x=100,y=50)
        self.e1.place(x=300,y=50)
        self.l1.place(x=label_x,y=label_y)
        self.e1.place(x=entry_x,y=entry_y)


        self.var.trace_add("write", self.on_var_change)

    def on_var_change(self, *args):
        user_input = self.var.get()
        # print("User input:", user_input)

if __name__ == "__main__":
    root = Tk()
    f = Frame(root,width=1000,height=600,bg='#0E2954')  
    root.title("Budget Tracker")
    mb = UserNameEntry(f)
    root.mainloop()
