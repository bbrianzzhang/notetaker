from tkinter import *
from summarize import get_notes
from record import generate_recording
from transcribe_google import transcribe_file
import time
import concurrent.futures
import threading

root = Tk()
root.title("LazyNote")

recording = BooleanVar(root, False)
def start_recording():
    startButton["state"] = DISABLED
    endButton["state"] = NORMAL
    recording.set(True)
    f = open("transcription.txt", "w")
    f.write("")
    f.close()
    thread = threading.Thread(target=generate_recording)
    thread.start()
    root.after(10000, get_transcription)

def stop_recording():
    startButton["state"] = NORMAL
    endButton["state"] = DISABLED
    transcriptionButton["state"] = NORMAL
    notesButton["state"] = NORMAL
    root.after(10000, perma_stop)

def perma_stop():
    recording.set(False)

def get_transcription():
    if recording.get() == True:
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     future = executor.submit(transcribe_file, 'output.wav')
        #     return_val = future.result()
        #     print(return_val)
        # thread2 = threading.Thread(target=transcribe_file)
        # thread2.start()
        thread = threading.Thread(target=generate_recording)
        thread.start()
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     print("dawg")
        #     future = executor.submit(transcribe_file, 'output.wav')
        #     return_val=future.result()
        #     print(return_val)
        root.after(10000, get_transcription)

def make_notes():
    raw = open('transcription.txt', 'r')
    rawString = raw.read()
    notesName = notesFile.get()+".txt"
    notes = get_notes(rawString)
    file = open(notesName, "w")
    file.write(notes)
    file.close()
    print("Notes written!")

intro = Label(root, text="Welcome to LazyNote", width=40)
intro.grid(row=0, column=0, columnspan=2)
startButton = Button(root, text="start recording", width=40, height="2", command=start_recording)
endButton = Button(root, text="end recording", width=40, height="2", command=stop_recording, state="DISABLED")

transcribeFile = Entry(root, width=20)

transcriptionButton = Button(root,
    text="download transcription",
    width=20,
    state="DISABLED")

notesFile = Entry(root, width=20)

notesButton = Button(root,
    text="download automatic notes",
    width=20,
    command=make_notes,
    state="DISABLED")

startButton.grid(row=1, columnspan=2)
endButton.grid(row=2, columnspan=2)
transcribeFile.grid(row=3, column=0, columnspan=1)
transcribeFile.insert(0, "File name:")
transcriptionButton.grid(row=3, column=1, columnspan=1)
notesFile.grid(row=4, column=0, columnspan=1)
notesFile.insert(0, "File name:")
notesButton.grid(row=4, column=1, columnspan=1)

root.mainloop()
