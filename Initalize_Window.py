from git import *
import os as os
from tkinter import *
import sys
import os
import webbrowser
from Welcome_Page import *


class Initalize_Window:
    def __init__(self):
        self.signInRoot= Tk()
        self.root = Tk()
        signInPage = Welcome_Page(self.signInRoot,self.root)
        self.root.title('Githon')
        self.root.geometry('600x500')
        self.leftFrame = Frame(self.root, width=200)
        self.leftFrame.grid(row=1,column=0)
        self.root.mainloop()





