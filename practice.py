from tkinter import *
def just_buttons():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.minsize(width=500, height=300)
window.title("button creation")
window.config(pady=200, padx=100)

button = Button(text="click here", command=just_buttons)
button.grid(column=1, row=1)
yes_button = Button(text="click yes")
yes_button.grid(column=2, row=0)

def No_button():
    print("no")
    new_text = input.get()
    my_label.config(text=new_text)


No_button = Button(text="click No", command=No_button)
No_button.grid(column=1, row=0)


my_label = Label(text="doing what i know", font=("Arial", 8, "bold"),)
my_label.config(padx=20, pady=20)
my_label.grid(column=0, row=0)

input = Entry(width=10)
input.grid(column=2, row=1)
print(input.get())








window.mainloop()