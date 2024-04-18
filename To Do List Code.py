from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('600x550+600+300')
ws.title(' Chiranjeev To do List')
ws.config(bg='light yellow')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=20)

lb = Listbox(
    frame,
    width=30,
    height=10,
    font=('Times', 20),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='blue',
    activestyle="none",
    bg="light grey"
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat Fruits ',
    'drink water',
    'go gym',
    'write Code',
    'write Assignment',
    'take a nap',
    'Learn new skill',
    ' Drink protein shake'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 28)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='green',
    padx=25,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='red',
    padx=25,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()

