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
    sv_ttk.set_theme("dark")
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
      

      return

if __name__ == '__main__':
  app = MainApplication()
  row = MainApplication.PhotoRow()
  app.mainloop()

#file = re.search(r"(?<=folder:)\/[^;]+", f.read())