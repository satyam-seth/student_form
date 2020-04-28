import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.maxsize(288, 298)
win.minsize(288, 298)
win.title('Student Form')

# roll_num
roll_num_var = tk.StringVar()
roll_num_label = ttk.Label(win, text='Roll Number:')
roll_num_entrybox = ttk.Entry(win, width=16, textvariable=roll_num_var)
roll_num_label.grid(row=0, column=0, sticky=tk.W)
roll_num_entrybox.grid(row=0, column=1)
roll_num_entrybox.focus()

# s_name
s_name_var = tk.StringVar()
s_name_label = ttk.Label(win, text='Student Name:')
s_name_entrybox = ttk.Entry(win, width=16, textvariable=s_name_var)
s_name_label.grid(row=1, column=0, sticky=tk.W)
s_name_entrybox.grid(row=1, column=1)

# f_name
f_name_var = tk.StringVar()
f_name_label = ttk.Label(win, text='Father Name:')
f_name_entrybox = ttk.Entry(win, width=16, textvariable=f_name_var)
f_name_label.grid(row=2, column=0, sticky=tk.W)
f_name_entrybox.grid(row=2, column=1)

# email
email_var = tk.StringVar()
email_label = ttk.Label(win, text='Email:')
email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)
email_label.grid(row=3, column=0, sticky=tk.W)
email_entrybox.grid(row=3, column=1)

# phone_num
phone_num_var = tk.StringVar()
phone_num_label = ttk.Label(win, text='Phone Number:')
phone_num_entrybox = ttk.Entry(win, width=16, textvariable=phone_num_var)
phone_num_label.grid(row=4, column=0, sticky=tk.W)
phone_num_entrybox.grid(row=4, column=1)

# gender
gender_var = tk.StringVar()
gender_label = ttk.Label(win, text='Gender:')
gender_comobox = ttk.Combobox(
    win, width=13, textvariable=gender_var, state='readonly')
gender_comobox['values'] = ('Male', 'Female', 'Others')
gender_comobox.current(0)
gender_label.grid(row=5, column=0, sticky=tk.W)
gender_comobox.grid(row=5, column=1)

# highschool detatils
highschool_ptg_var = tk.StringVar()
highschool_ptg_label = ttk.Label(win, text='10th Percentage:')
highschool_ptg_entrybox = ttk.Entry(
    win, width=16, textvariable=highschool_ptg_var)
highschool_board_var = tk.StringVar()
highschool_board_label = ttk.Label(win, text='10th Board Name:')
radio_btn1 = ttk.Radiobutton(
    win, text='UP Board', value='UP Board', variable=highschool_board_var)
radio_btn2 = ttk.Radiobutton(
    win, text='CBSE Board', value='CBSE Board', variable=highschool_board_var)
radio_btn3 = ttk.Radiobutton(
    win, text='ICSE Board', value='ICSE Board', variable=highschool_board_var)
radio_btn4 = ttk.Radiobutton(
    win, text='Others', value='Others', variable=highschool_board_var)
highschool_ptg_label.grid(row=6, column=0, sticky=tk.W)
highschool_ptg_entrybox.grid(row=6, column=1)
highschool_board_label.grid(row=7, column=0, sticky=tk.W)
radio_btn1.grid(row=7, column=1, sticky=tk.W)
radio_btn2.grid(row=7, column=2, sticky=tk.W)
radio_btn3.grid(row=8, column=1, sticky=tk.W)
radio_btn4.grid(row=8, column=2, sticky=tk.W)

# intermediate detatils
inter_ptg_var = tk.StringVar()
inter_ptg_label = ttk.Label(win, text='12th Percentage:')
inter_ptg_entrybox = ttk.Entry(win, width=16, textvariable=inter_ptg_var)
inter_board_var = tk.StringVar()
inter_board_label = ttk.Label(win, text='12th Board Name:')
radio_btn5 = ttk.Radiobutton(
    win, text='UP Board', value='UP Board', variable=inter_board_var)
radio_btn6 = ttk.Radiobutton(
    win, text='CBSE Board', value='CBSE Board', variable=inter_board_var)
radio_btn7 = ttk.Radiobutton(
    win, text='ICSE Board', value='ICSE Board', variable=inter_board_var)
radio_btn8 = ttk.Radiobutton(
    win, text='Others', value='Others', variable=inter_board_var)
inter_ptg_label.grid(row=9, column=0, sticky=tk.W)
inter_ptg_entrybox.grid(row=9, column=1)
inter_board_label.grid(row=10, column=0, sticky=tk.W)
radio_btn5.grid(row=10, column=1, sticky=tk.W)
radio_btn6.grid(row=10, column=2, sticky=tk.W)
radio_btn7.grid(row=11, column=1, sticky=tk.W)
radio_btn8.grid(row=11, column=2, sticky=tk.W)

# college website registered or not
check_btn_var = tk.IntVar()
check_btn = ttk.Checkbutton(
    win, text='I have registered on college attendance portal.', variable=check_btn_var)
check_btn.grid(row=12, columnspan=3)

# action


def action():
    roll_num = roll_num_var.get()
    s_name = s_name_var.get()
    f_name = f_name_var.get()
    email = email_var.get()
    phone_num = phone_num_var.get()
    gender = gender_var.get()
    highschool_ptg = highschool_ptg_var.get()
    highschool_board = highschool_board_var.get()
    inter_ptg = inter_ptg_var.get()
    inter_board = inter_board_var.get()
    if check_btn_var.get() == 0:
        register = 'Not Registered'
    else:
        register = 'Registered'

    # wirte to csv file
    with open('data.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['Roll Number', 'Student Name', 'Father\'s Name', 'Email Address', 'Phone Number', 'Gender',
                                                'High School Percentage', 'High School Board', 'Intermediate Percentage', 'Intermediate Board', 'Attendance Portal Registration Status'])
        if os.stat('data.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Roll Number': roll_num,
            'Student Name': s_name,
            'Father\'s Name': f_name,
            'Email Address': email,
            'Phone Number': phone_num,
            'Gender': gender,
            'High School Percentage': highschool_ptg,
            'High School Board': highschool_board,
            'Intermediate Percentage': inter_ptg,
            'Intermediate Board': inter_board,
            'Attendance Portal Registration Status': register
        })

    roll_num_entrybox.delete(0, tk.END)
    s_name_entrybox.delete(0, tk.END)
    f_name_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    phone_num_entrybox.delete(0, tk.END)
    highschool_ptg_entrybox.delete(0, tk.END)
    inter_ptg_entrybox.delete(0, tk.END)


# submit button
submit_btn = ttk.Button(win, text='Submit', command=action)
submit_btn.grid(row=13, column=1)

win.mainloop()
