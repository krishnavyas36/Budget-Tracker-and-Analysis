from tkinter import *
from ui_assets.submit_button import SubmitButton
from ui_assets.username_entry import UserNameEntry

root = Tk()

finalFrame = Frame(root,height=700, width=1100)  #,bg='#151617'

root.title("Budget Tracker")
# root.config(background='#272829')
root.geometry("1360x760")
finalFrame.pack() 

def get_data_on_submit():
    

    username_entry = UserNameEntry(finalFrame, "Username", 100,50,300,50)
    date_entry = UserNameEntry(finalFrame, "Date", 100,100,300,100)
    description_entry = UserNameEntry(finalFrame, "Description", 100,150,300,150)
    category_entry = UserNameEntry(finalFrame, "Category", 100,200,300,200)
    amount_entry = UserNameEntry(finalFrame, "Amount", 100,250,300,250)

    submit_button = SubmitButton(finalFrame, X)  

    submit_button.submitButton.config(command=lambda: finalFrame.quit()) 

    root.mainloop() 

    return [username_entry.var.get(),date_entry.var.get(),description_entry.var.get(),category_entry.var.get(),amount_entry.var.get()] 