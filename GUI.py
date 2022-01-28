from tkinter import *
import logging
from typing import List

from PyPDF2 import PdfFileMerger
import os
logging.basicConfig(filename = 'test.log', level = logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s")

pdfs = []

def clear():
    T.delete(1.0,END)
def all_file():
    """Function to return files in a directory"""
    path1 = par.get()
    path = os.listdir(path1)
    global pdfs

    try:
        test = 0
        for i in path:
                pdfs.append(i)
        T.insert(END,pdfs)
        for i in pdfs:
            if i.endswith('pdf'):
                test += 1
        if test > 1:
            print("More than 1 pdf file exists merge?")
            T.insert(END,"\n\nMore than 1 pdf file exists merge?")
            pop_up()


    except Exception as e:
        T.insert(1.0,e)
        logging.error("Error occured {}".format(e))


def merger():
    """Program to merge pdfs"""
    path = par.get()
    main_path = []
    dirs = os.listdir(path)
    for i in dirs:
        if i.endswith('pdf'):
            main_path.append(i)
    merger_main = PdfFileMerger()
    try:
        for i in main_path:
            if i.endswith('pdf'):
                merger_main.append(i)
        merger_main.write('Merged_file.pdf')
        merger_main.close()
    except Exception as e:
        logging.error("Error occured {}".format(e))
        print(e)

def pop_up():
    a = Toplevel(root)
    a.geometry("200x200")
    Label(a, text = "Merge PDF?").pack()
    T1 = Text(a,height = 10, width = 10)
    T1.pack()
    Button(a,text = "Merge multiple pdfs",command= merger).pack()
    a.title("PDF MERGER")
    a.mainloop()


root = Tk()
root.geometry('300x300')
root.title("PDF Merger")
Label(root, text = 'PDF MERGER').pack()
Label(root,text = 'Enter working directory to search for:').pack()
par = StringVar()
Main = Entry(root,textvariable=par)
Main.pack()

Button(root, text = 'Enter to show all files in the directory', command= all_file).pack()
T = Text(root, height= 5,width=30, wrap = 'word')
T.config(state = 'normal')
T.pack()
Button(root,text = 'clear', command = clear).pack()



root.mainloop()