from git import *
import os as os
from read_repo import *
from tkinter import *
import sys
import os
import webbrowser
from AccessMethods import *
from functools import *

class Welcome_Page:
	def __init__(self, root, frame):
		self.root = root
		self.frame = frame
		self.welcome_label = Label(self.frame, text='Welcome to Githon, Log in Below!',font=('Rouge',10))
		self.ghUsernameLabel = Label(self.frame,text='Username')
		self.ghUsernameEntry = Entry(self.frame, borderwidth= 2)
		self.ghPasswordLabel = Label(self.frame,text='Password')
		self.ghPasswordEntry = Entry(self.frame, borderwidth= 2)
		self.ghLoginButton = Button(self.frame, text='Login!', command=lambda: login(self.ghUsernameEntry.get(),self.ghPasswordEntry.get()))






		#Grid Assignements
		self.welcome_label.grid(column=1)
		self.ghUsernameLabel.grid(row=1)
		self.ghUsernameEntry.grid(row=1,column=1)
		self.ghPasswordLabel.grid(row=2)
		self.ghPasswordEntry.grid(row=2,column=1)
		self.ghLoginButton.grid(row=3,column=1)
