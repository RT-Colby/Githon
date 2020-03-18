from git import *
import os as os
from read_repo import *
from tkinter import *
import sys
import os
import webbrowser

class Welcome_Page:
	def __init__(self, root, frame):
		self.root = root
		self.frame = frame
		self.welcome_label = Label(self.frame, text='Welcome to Githon, \n The Python Based Git Client')
		self.welcome_label.grid()
		self.ghUsername = Entry(self.frame)