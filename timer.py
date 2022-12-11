# ADeveloper : Samarth Pai
# Date : 11 December 2022
# Program : GUI Stopwatch
# Note : Press spacebar for play/pause and press r to reset

from tkinter import Label, Frame, Tk, font
import time, datetime

root = Tk()
font.Font()
root.title("Stopwatch")
root.geometry("250x100")
startMode = 0


def control(event):
    global iTime
    global startMode
    startMode = 1
    if timeStr == "00:00:000":
        iTime = time.time()
    root.unbind("<space>")
    root.bind("<space>", stop)
    return timeSetter(timeStr)


def stop(event):
    global startMode, spentTime
    startMode = 0
    spentTime = time.time() - iTime
    root.unbind("<space>")
    root.bind("<space>", control)


def timeSetter(event):
    global msIs1000, timeLabel, timeStr, spentTime
    timeStr = datetime.datetime.fromtimestamp(28751400.0 + spentTime).strftime(
        "%M:%S:%f"
    )[:-3]
    spentTime = time.time() - iTime
    timeLabel["text"] = timeStr
    if startMode:
        root.after(1, lambda: timeSetter(timeStr))
    else:
        return 0


def reset(event):
    global timeStr, startMode, iTime, spentTime
    spentTime = 0
    startMode = 0
    timeStr = "00:00:000"
    iTime = time.time()
    timeLabel["text"] = timeStr


timeStr = "00:00:000"

spentTime = 0
timeFrame = Frame(height=200, width=200)
timeFrame.place(relx=0.5, rely=0.5, anchor="center")
timeLabel = Label(timeFrame, text=timeStr, font="Arial 30 bold")
timeLabel.pack()

root.bind("<r>", reset)
root.bind("<space>", control)
root.mainloop()