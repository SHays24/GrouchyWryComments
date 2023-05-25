from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sv_ttk
import re


class MainApplication(Tk):
  def __init__(self):
    self.started = False
    super().__init__()
    try:
      open("settings.txt", "r")
    except:
      setFolder() 
    self.title("Galeri")
    chatterbox = PhotoImage(file = "./chatterbox.png")
    self.iconphoto(False, chatterbox)
    self.nb = ttk.Notebook(self)
    sv_ttk.set_theme("light")
  def setFolder():
    folder = filedialog.askdirectory()
    f = open("settings.txt", "wt")
    f.write("folder:" + folder + ";")
    f.close()
  try:
    open("settings.txt", "r")
  except:
    setFolder()
  class PhotoRow(Tk):
    def __init__(self):
      f = open("settings.txt", "r")
      file = re.search(r"(?<=folder:)\/[^;]+", f.read())
      print(file.group())
      return

if __name__ == '__main__':
  app = MainApplication()
  row = MainApplication.PhotoRow()
  app.mainloop()
"""
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="", wraplength=200).grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
"""
