"""
Have to encase the GUI and the update in different threads
"""

from tkinter import *
import tkinter.messagebox as tmsg
sub_number = 0


def check():
    with open("Subtitle.txt", "w") as f:
        f.write(ShowArea.get(1.0, END))


def update():
    ShowArea.delete(1.0, END)
    with open("Subtitle.txt", "r") as f:
        ShowArea.insert(1.0, f.read())


def writing_the_file():
    global sub_number
    if TextArea.get(1.0, END) != "\n":
        with open("Subtitle.txt", "a") as f:
            f.writelines([str(sub_number), "\n", startting_time.get(), " --> ", ending_time.get(), "\n", TextArea.get(1.0, END)])
        clear_area()
        sub_number += 1
        update()
    else:
        tmsg.showinfo("No Subtitle Entered", "Please enter subtitle in the text area.")


def clear_area():
    TextArea.delete(1.0, END)
    startting_time.set("00:00:00,000")
    ending_time.set("00:00:00,000")


root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)
root.wm_iconbitmap("notepad.ico")
root.title("Zander's Subtitle Editor")
root.config(bg="gray25")
Label(root, text="Starting Time", font="cambria 16", bg="gray25", fg="light cyan").place(relx=0.17, rely=0.1)
Label(root, text="(HH:MM:SS,DIV)", font="cambria 10", bg="gray25", fg="light cyan").place(relx=0.185, rely=0.15)
Label(root, text="Ending Time", font="cambria 16", bg="gray25", fg="light cyan").place(relx=0.7, rely=0.1)
Label(root, text="(HH:MM:SS,DIV)", font="cambria 10", bg="gray25", fg="light cyan").place(relx=0.710, rely=0.15)
startting_time = StringVar()
startting_time.set("00:00:00,000")
startting_timeentry = Entry(root, textvar=startting_time, font="Calibri 11", width=18, justify=CENTER, bg="gray25", fg="cyan2")
startting_timeentry.place(relx=0.17, rely=0.2)
ending_time = StringVar()
ending_time.set("00:00:00,000")
ending_timeentry =Entry(root, textvar=ending_time, font="Calibri 11", width=18, justify=CENTER, bg="gray25", fg="cyan2")
ending_timeentry.place(relx=0.7, rely=0.2)
Label(root, text="Enter Subtitle Text Here", font="Calibri 24", bg="gray25", fg="light cyan").place(relx=0.337, rely=0.3)
TextArea = Text(root, font="Calibri 12", width=83, height=2, wrap=WORD, bg="gray25", fg="cyan2")
TextArea.place(relx=0.17, rely=0.4)
enter_sub = Button(root, text="Enter Subtitle", command=writing_the_file, bg="gray25", fg="SpringGreen2")
enter_sub.place(relx=0.26, rely=0.9, width=100, height=35)
Button(root, text="Update Subtitle", command=check, bg="gray25", fg="SpringGreen2").place(relx=0.66, rely=0.9, width=100, height=35)
ShowArea = Text(root, font="Calibri 12", width=83, height=12, wrap=WORD, bg="gray25", fg="green2")
ShowArea.place(relx=0.17, rely=0.5)
root.mainloop()
