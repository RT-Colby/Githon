from git import *
import os as os
from read_repo import *
from tkinter import *
import sys
import os
import webbrowser
from AccessMethods import *
from functools import *
import tkinter.ttk as tkrtk


class Welcome_Page:
	def __init__(self,root,client):
		self.root = root
		self.root.title('Githon Sign in')
		self.root.geometry('300x150')
		self.welcome_label = Label(self.root, text='Welcome to Githon, Log in Below!',font=('Rouge',10))
		self.ghUsernameLabel = Label(self.root,text='Username')
		self.ghUsernameEntry = Entry(self.root, borderwidth= 2)
		self.ghPasswordLabel = Label(self.root,text='Password')
		self.ghPasswordEntry = Entry(self.root, borderwidth= 2)
		self.repoNB = tkrtk.Notebook(client)
		self.ghLoginButton = Button(self.root, text='Login!', command=lambda: login(self,client,self.repoNB,self.ghUsernameEntry.get(),self.ghPasswordEntry.get(),self.root))
		#Notebook

		#Grid Assignements
		self.welcome_label.grid(column=1)
		self.ghUsernameLabel.grid(row=1)
		self.ghUsernameEntry.grid(row=1,column=1)
		self.ghPasswordLabel.grid(row=2)
		self.ghPasswordEntry.grid(row=2,column=1)
		self.ghLoginButton.grid(row=3,column=1)



