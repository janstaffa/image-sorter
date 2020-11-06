import os, time, datetime, shutil, tkinter
from tkinter import filedialog
import PIL.Image
from datetime import datetime


window = tkinter.Tk()

window.title("File sorter")

window.geometry('300x60')

lbl = tkinter.Label(window, text="No folder selected...")
lbl.grid(column=0, row=0)

def search():
    window.directory = filedialog.askdirectory()
    lbl.configure(text= window.directory)

searchBtn = tkinter.Button(window, text="Browse", command=search)
searchBtn.grid(column=1, row=0)


def clicked():
    path = window.directory+"/"
    files = os.listdir(path)

    for file in files: 
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            print(file) 
            date_taken = PIL.Image.open(path+file)._getexif()[36867]
            date = datetime.strptime(date_taken, '%Y:%m:%d %H:%M:%S')
            print(date)

            month = ""
            m = date.strftime("%m")
            if m == "01":
                month = "January"
            elif m == "02":
                month = "February"
            elif m == "03":
                month = "March"
            elif m == "04":
                month = "April"
            elif m == "05":
                month = "May"
            elif m == "06":
                month = "June"
            elif m == "07":
                month = "July"
            elif m == "08":
                month = "August"
            elif m == "09":
                month = "September"
            elif m == "10":
                month = "October"
            elif m == "11":
                month = "November"
            elif m == "12":
                month = "December"
            else:
                month = "INVALID MONTH"

            if not os.path.isdir(path+str(date.year)):
                os.mkdir(path+str(date.year))
            if not os.path.isdir(path+str(date.year)+"/"+month):
                os.mkdir(path+str(date.year)+"/"+month)
            if not os.path.isdir(path+str(date.year)+"/"+month+"/"+str(date.day)):
                os.mkdir(path+str(date.year)+"/"+month+"/"+str(date.day))
            shutil.move(path+file, path+str(date.year)+"/"+month+"/"+str(date.day))

    lbl.configure(text="done")

btn = tkinter.Button(window, text="Sort", command=clicked)
btn.grid(column=2, row=0)


window.mainloop()


        

