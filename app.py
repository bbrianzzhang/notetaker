from tkinter import *

root = Tk()
root.title("note taker")

def myClick():
    return

intro = Label(root, text="Welcome to Note Taker", width=40)
intro.grid(row=0, column=0, columnspan=2)
startButton = Button(root, text="start recording", width=40, height="2", command="")
endButton = Button(root, text="end recording", width=40, height="2", command="")

transcribeFile = Entry(root, width=20)

transcriptionButton = Button(root,
    text="download transcription",
    width=20,
    state="disabled")

notesFile = Entry(root, width=20)

notesButton = Button(root,
    text="download automatic notes",
    width=20,
    state="disabled")

startButton.grid(row=1, columnspan=2)
endButton.grid(row=2, columnspan=2)
transcribeFile.grid(row=3, column=0, columnspan=1)
transcribeFile.insert(0, "File name:")
transcriptionButton.grid(row=3, column=1, columnspan=1)
notesFile.grid(row=4, column=0, columnspan=1)
notesFile.insert(0, "File name:")
notesButton.grid(row=4, column=1, columnspan=1)

root.mainloop()
# def only_numbers(char):
#  return char.replace(".", "0", 1).isdigit()
#
# def add_val():
#  added_val = int(number1.get()) +  int(number2.get())
#  label3 = tk.Label(root, width=60, text =  "SUM " + str(added_val), anchor = 'w')
#  label3.config(font=("Raleway",18))
#  label3.pack(side=tk.LEFT, padx=150, ipady = 100)
#
# root = tk.Tk()
# root.title("Desktop Application")
# root.geometry("750x500")
#
# label = tk.Label(root, width=22, text="Addition of two numbers", anchor='w')
# label.config(font=("Raleway",16))
# label.pack(side=tk.TOP, pady = 30)
#
# row = tk.Frame(root)
# label = tk.Label(row, width=22, text="Number 1", anchor='w')
# label.config(font=("Raleway",16))
#
# validation = row.register(only_numbers)
# number1 = tk.Entry(row, validate="key", validatecommand=(validation, %S'))
# number1.config(font=("Raleway",16))
#
# row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# label.pack(side=tk.LEFT)
# number1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
#
# row2 = tk.Frame(root)
# label2 = tk.Label(row2, width=22, text="Number 2", anchor='w')
# label2.config(font=("Raleway",16))
# validation = row2.register(only_numbers)
# number2 = tk.Entry(row2, validate="key", validatecommand=(validation, '%S'))
# number2.config(font=("Raleway",16))
#
# row2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
# label2.pack(side=tk.LEFT)
# number2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
#
# b1 = tk.Button(root, width = 15, text='Add', background = "Light green", command=(lambda: add_val()))
# b1.config(font=("Raleway", 18))
# b1.pack(side=tk.RIGHT, padx=5, pady=5)
