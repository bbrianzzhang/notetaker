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
