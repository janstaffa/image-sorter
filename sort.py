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
                month = "Leden"
            elif m == "02":
                month = "Únor"
            elif m == "03":
                month = "Březen"
            elif m == "04":
                month = "Duben"
            elif m == "05":
                month = "Květen"
            elif m == "06":
                month = "Červen"
            elif m == "07":
                month = "Červenec"
            elif m == "08":
                month = "Srpen"
            elif m == "09":
                month = "Září"
            elif m == "10":
                month = "Říjen"
            elif m == "11":
                month = "Listopad"
            elif m == "12":
                month = "Prosinec"
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


        

