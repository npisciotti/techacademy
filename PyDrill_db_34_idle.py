import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil, os, stat, time, datetime, glob, sqlite3
from datetime import timedelta

#Define class

class FileCheck():
    #Frame is the Tkinter frame class that our own class will inherit from


        def __init__(self, master):
           



            #Initialize your class and Tkinter master-level frame
            #define the master frame configuration
            self.master = master
            self.master.minsize(500, 300) #setting (Height, Width)

            # This CenterWindow method will center the app on the user's screen
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
            self.t1.set(folderInput)

        def outputFolder(self):
            folderOutput = filedialog.askdirectory()
            print("folderOutput: {}".format(folderOutput))
            self.t2.set(folderOutput)

        def transfer(self):
            fileFrom = self.t1.get()
            fileTo = self.t2.get()
            today1 = datetime.datetime.today()
            last24Hours = str(today1 - timedelta(hours=24))
            print(today1)

            for file in glob.glob(os.path.join(fileFrom, '*.txt')):
                epochDate = os.path.getmtime(file)
                modifiedDate = datetime.datetime.fromtimestamp(int(epochDate)).strftime('%Y-%m-%d %H:%M:%S')
                if modifiedDate > last24Hours:
                    shutil.move(file, fileTo)
                self.t3.set(today1)
                dbToday = time.time()
                print("dbToday: {}".format(dbToday))
                self.data_entry(dbToday) #don't use global variables! It is better to pass in today to your database function

        def create_table(self):
            conn = sqlite3.connect('transfersDate.db')
            with conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS date (time REAL)")
            conn.commit()
            conn.close()

        def data_entry(self,dbToday):
            conn = sqlite3.connect('transfersDate.db')
            with conn:
                c = conn.cursor()
                c.execute("INSERT INTO date (time) VALUES(?)""",(dbToday))
            conn.commit()
            c.close()
            conn.close()    

def main():

    root = Tk()
    App = FileCheck(root)
    root.mainloop()
    
    
if __name__ == "__main__": main()
