import tkinter as tk
import tkinter.font as tkFont
import os
import sys
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from os.path import splitext

	
root = tk.Tk()
root.title("Folder Locker")
root.geometry("250x70")
root.resizable(width=False, height=False)

def lockFolder():
	folder_selected = filedialog.askdirectory()
	path = folder_selected
	path = path.replace('"','')
	path = path.replace("\\","/")
	name, ext = splitext(path)
	file = name + ".{2559a1f2-21d7-11d4-bdaf-00c04f60b9f0}"
	os.rename(name,file)
	messagebox.showinfo("Information","Locked")    

def unlockFolder():
	filename =  filedialog.askopenfilename()
	path = filename
	path = path.replace('"','')
	path = path.replace("\\","/")
	name, ext = splitext(path)
	os.rename(path,name)
	messagebox.showinfo("Information","UnLocked")


lockBtn = tk.Button(root)
lockBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=15)
lockBtn["font"] = ft
lockBtn["fg"] = "#FCC201"
lockBtn["justify"] = "center"
lockBtn["text"] = "Lock"
lockBtn["relief"] = "groove"
lockBtn.place(x=30,y=20,width=80,height=30)
lockBtn["command"] = lockFolder

unlockBtn = tk.Button(root)
unlockBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=15)
unlockBtn["font"] = ft
unlockBtn["fg"] = "#4DD0E1"
unlockBtn["justify"] = "center"
unlockBtn["text"] = "UnLock"
unlockBtn["relief"] = "groove"
unlockBtn.place(x=140,y=20,width=80,height=30)
unlockBtn["command"] = unlockFolder

root.mainloop()