from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sv_ttk
import re
import os


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
    
  def IndexFoto(directory, pos):
    index = os.listdir(directory)
    index.sort()
    if pos < 0 | pos >= len(index):
      return None
    name = index[pos]
    path = os.path.join(directory, name)
    return path
    
    
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
      
      

      return

if __name__ == '__main__':
  app = MainApplication()
  row = MainApplication.PhotoRow()
  app.mainloop()

#file = re.search(r"(?<=folder:)\/[^;]+", f.read())