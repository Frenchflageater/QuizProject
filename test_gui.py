# imports
from tkinter import *
from tkinter import ttk


# functions
def get_var():
    item = radio_var.get()
    print(item)
    if radio_text.get() == 'A1-1':
        if item == 'a1':
            print('correct')
            feedback.set('correct')
            question_text.set('Q2')
            radio_text.set('A1-2')
            radio_text2.set('A2-2')
            radio_text3.set('A3-2')
        else:
            print('incorrect')
            feedback.set('incorrect')
            question_text.set('Q2')
            radio_text.set('A1-2')
            radio_text2.set('A2-2')
            radio_text3.set('A3-2')
    elif radio_text.get() == 'A1-2':
        if item == 'a2':
            print('correct')
            feedback.set('correct')
            question_text.set('Q3')
            radio_text.set('A1-3')
            radio_text2.set('A2-3')
            radio_text3.set('A3-3')
        else:
            print('incorrect')
            feedback.set('incorrect')
            question_text.set('Q3')
            radio_text.set('A1-3')
            radio_text2.set('A2-3')
            radio_text3.set('A3-3')
    elif radio_text.get() == 'A1-3':
        if item == 'a3':
            print('correct')
            feedback.set('correct')
        else:
            print('incorrect')
            feedback.set('incorrect')


# gui
root = Tk()
root.title('Test GUI')

frame = Frame(root, bg='light blue')
frame.grid(row=0, column=0)

frame2 = Frame(frame, bg='light blue')
frame2.grid(row=1, column=0)

# label variables
question_text = StringVar()
question_text.set('Q1')
feedback = StringVar()
feedback.set(' ')

label = Label(frame, width=20, height=2, bg='light blue', textvariable=question_text)
label.grid(row=0, column=0)

label2 = Label(frame, width=20, height=2, bg='light blue', textvariable=feedback)
label2.grid(row=2, column=0)

# radio style
s = ttk.Style()
s.configure('Style1.TRadiobutton',
            background='light blue')

# radio variables
radio_var = StringVar()
radio_text = StringVar()
radio_text.set('A1-1')
radio_text2 = StringVar()
radio_text2.set('A2-1')
radio_text3 = StringVar()
radio_text3.set('A3-1')

# radio buttons
radio1 = ttk.Radiobutton(frame2, textvariable=radio_text, value='a1', variable=radio_var,
                         command=get_var, style='Style1.TRadiobutton')
radio1.grid(row=0, column=0, pady=5)
radio2 = ttk.Radiobutton(frame2, textvariable=radio_text2, value='a2', variable=radio_var,
                         command=get_var, style='Style1.TRadiobutton')
radio2.grid(row=1, column=0)
radio3 = ttk.Radiobutton(frame2, textvariable=radio_text3, value='a3', variable=radio_var,
                         command=get_var, style='Style1.TRadiobutton')
radio3.grid(row=2, column=0, pady=5)

# run
root.mainloop()
