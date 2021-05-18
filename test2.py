# imports
from tkinter import *
from tkinter import ttk


# functions
def q1_answer():
    if radio_var.get() == 'a1':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q2_answer():
    if radio_var.get() == 'a2':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q3_answer():
    if radio_var.get() == 'a3':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q4_answer():
    if radio_var.get() == 'a1':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q5_answer():
    if radio_var.get() == 'a2':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q6_answer():
    if radio_var.get() == 'a3':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q7_answer():
    if radio_var.get() == 'a1':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q8_answer():
    if radio_var.get() == 'a2':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q9_answer():
    if radio_var.get() == 'a3':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def q10_answer():
    if radio_var.get() == 'a1':
        print('correct')
        feedback.set('correct')
        score.set(score.get() + 1)
        print(score.get())
    else:
        print('incorrect')
        feedback.set('incorrect')
        print(score.get())
    radio1.configure(state=DISABLED)
    radio2.configure(state=DISABLED)
    radio3.configure(state=DISABLED)


def answer_checker():
    if radio_text.get() == 'A1-1':
        q1_answer()
    elif radio_text.get() == 'A1-2':
        q2_answer()
    elif radio_text.get() == 'A1-3':
        q3_answer()
    elif radio_text.get() == 'A1-4':
        q4_answer()
    elif radio_text.get() == 'A1-5':
        q5_answer()
    elif radio_text.get() == 'A1-6':
        q6_answer()
    elif radio_text.get() == 'A1-7':
        q7_answer()
    elif radio_text.get() == 'A1-8':
        q8_answer()
    elif radio_text.get() == 'A1-9':
        q9_answer()
    elif radio_text.get() == 'A1-10':
        q10_answer()


def next_q():
    if radio_text.get() == 'A1-1':
        question_text.set('Q2')
        feedback.set('')
        radio_text.set('A1-2')
        radio_text2.set('A2-2')
        radio_text3.set('A3-2')
    elif radio_text.get() == 'A1-2':
        question_text.set('Q3')
        feedback.set('')
        radio_text.set('A1-3')
        radio_text2.set('A2-3')
        radio_text3.set('A3-3')
    elif radio_text.get() == 'A1-3':
        question_text.set('Q4')
        feedback.set('')
        radio_text.set('A1-4')
        radio_text2.set('A2-4')
        radio_text3.set('A3-4')
    elif radio_text.get() == 'A1-4':
        question_text.set('Q5')
        feedback.set('')
        radio_text.set('A1-5')
        radio_text2.set('A2-5')
        radio_text3.set('A3-5')
    elif radio_text.get() == 'A1-5':
        question_text.set('Q6')
        feedback.set('')
        radio_text.set('A1-6')
        radio_text2.set('A2-6')
        radio_text3.set('A3-6')
    elif radio_text.get() == 'A1-6':
        question_text.set('Q7')
        feedback.set('')
        radio_text.set('A1-7')
        radio_text2.set('A2-7')
        radio_text3.set('A3-7')
    elif radio_text.get() == 'A1-7':
        question_text.set('Q8')
        feedback.set('')
        radio_text.set('A1-8')
        radio_text2.set('A2-8')
        radio_text3.set('A3-8')
    elif radio_text.get() == 'A1-8':
        question_text.set('Q9')
        feedback.set('')
        radio_text.set('A1-9')
        radio_text2.set('A2-9')
        radio_text3.set('A3-9')
    elif radio_text.get() == 'A1-9':
        question_text.set('Q10')
        feedback.set('')
        radio_text.set('A1-10')
        radio_text2.set('A2-10')
        radio_text3.set('A3-10')
        next_button.configure(text='end')
    else:
        print(f'score: {score.get()}')
        file = open('scores.txt', 'a')
        file.write(str(score.get()))
        file.close()
        feedback.set('')
        next_button.configure(state=DISABLED)
        radio1.configure(state=DISABLED)
        radio2.configure(state=DISABLED)
        radio3.configure(state=DISABLED)
        return
    radio1.configure(state=NORMAL)
    radio1.state(['!focus', '!selected'])
    radio2.configure(state=NORMAL)
    radio2.state(['!focus', '!selected'])
    radio3.configure(state=NORMAL)
    radio3.state(['!focus', '!selected'])
    next_button.configure(state=DISABLED)


def enable():
    next_button.configure(state=NORMAL)


# gui
root = Tk()
root.title('Test GUI')

score = IntVar()
score.set(0)

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
                         command=lambda: [answer_checker(), enable()], style='Style1.TRadiobutton')
radio1.grid(row=0, column=0, pady=5)
radio2 = ttk.Radiobutton(frame2, textvariable=radio_text2, value='a2', variable=radio_var,
                         command=lambda: [answer_checker(), enable()], style='Style1.TRadiobutton')
radio2.grid(row=1, column=0)
radio3 = ttk.Radiobutton(frame2, textvariable=radio_text3, value='a3', variable=radio_var,
                         command=lambda: [answer_checker(), enable()], style='Style1.TRadiobutton')
radio3.grid(row=2, column=0, pady=5)

# buttons
next_button = ttk.Button(frame2, text='next', command=next_q)
next_button.grid(row=3, pady=5)
next_button.configure(state=DISABLED)

# run
root.mainloop()
