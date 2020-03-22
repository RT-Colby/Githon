from git import *
from github import Github
import os as os
from tkinter import *
import sys
import os
import webbrowser
import tkinter.ttk as tkrtk
from tkinter import messagebox
from AccessMethods import * 
import git

class HomeWindow():
	def __init__(self,ghAcc,notebook):
		self.homeFrame = tkrtk.Frame(notebook, width=500, height=900)
		ghUser = ghAcc.get_user()
		welcome_message = 'Hello ' + ghUser.name + '\nYou are signed in as ' + ghUser.login
		self.NameLabel = Label(self.homeFrame,text=welcome_message, font=('TkDefaultFont',12))
		self.NameLabel.grid(row=0,column=0,sticky='NESW')
		notebook.add(self.homeFrame, text='Home')

