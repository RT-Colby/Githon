from git import *
import os as os
from tkinter import *
import sys
import os
import webbrowser
from Welcome_Page import *


class Initalize_Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Githon')
        self.root.geometry('500x300')
        self.leftFrame = Frame(self.root, width=200)
        self.leftFrame.grid()
        self.Welcomepage = Welcome_Page(self.root,self.leftFrame)



    def start(self):
        self.root.mainloop()



