import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil, os, stat, time, datetime, glob, sqlite3
from datetime import timedelta

#Define class

#set up sqlite cursor
conn = sqlite3.connect('transfers.db')
c = conn.cursor()

class FileCheck():
    #Frame is the Tkinter frame class that our own class will inherit from


        def __init__(self, master):
           



            #Initialize your class and Tkinter master-level frame
            #define the master frame configuration
            self.master = master
            self.master.minsize(500, 300) #setting (Height, Width)

            # This CenterWindow method will center our app on the user's screen
            self.master.title("File Transfer")
            self.master.configure(background="lightblue")

            self.t1 = StringVar()
            self.t2 = StringVar()
            self.t3 = StringVar()     
    
            self.button1 = ttk.Button(self.master, text = "Folder to update daily from.", width =
                                      30, command = self.inputFolder)
            self.button1.pack()
            self.txt1 = ttk.Entry(self.master, width = 50, textvariable = self.t1).pack()

            self.button2 = ttk.Button(self.master, text = "Folder to update daily to", width = 30,
                                      command = self.outputFolder)
            self.button2.pack()
            self.txt2 = ttk.Entry(self.master, width = 50, textvariable = self.t2).pack()

            self.button3 = ttk.Button(self.master, text = "Transfer everything modified in the past 24 hours",
                                      width = 50, command = self.transfer)
            self.button3.pack()
            self.Label = ttk.Label(text = "Last File Check time")
            self.txt3 = ttk.Entry(self.master, width = 50, textvariable = self.t3).pack()

        def inputFolder(self):
            folderInput = filedialog.askdirectory()
            print("folderInput: {}".format(folderInput))
            #label = Label(text=folderInput).pack()
            self.t1.set(folderInput)

        def outputFolder(self):
            folderOutput = filedialog.askdirectory()
            print("folderOutput: {}".format(folderOutput))
            #label = Label(text=folderOutput).pack()
            self.t2.set(folderOutput)

        def transfer(self):
            fileFrom = self.t1.get()
            fileTo = self.t2.get()
            today = datetime.datetime.today()
            last24Hours = str(today - timedelta(hours=24))
                
            for file in glob.glob(os.path.join(fileFrom, '*.txt')):
                epochDate = os.path.getmtime(file)
                modifiedDate = datetime.datetime.fromtimestamp(int(epochDate)).strftime('%Y-%m-%d %H:%M:%S')
                if modifiedDate > last24Hours:
                    shutil.move(file, fileTo)

            self.t3.set(today)
            return self.t3

        
        #def create_table():
        #    c.execute('CREATE TABLE IF NOT EXISTS dateOfTransfer(time REAL, datestamp TEXT, keyword TEXT, value REAL)')
        #def data_entry():
        #    c.execute('INSERT INTO dateOfTransfer VALUES(?,?,?)',(t3, phone, email))
            
            


#Python looks here first and runs the functions that fall below this line.

def main():

    root = Tk()
    App = FileCheck(root)
    root.mainloop()
    
if __name__ == "__main__": main()
