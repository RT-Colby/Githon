from git import *
import os as os
from tkinter import *
import sys
import os
import webbrowser
from functools import *
import tkinter.ttk as tkrtk
from RepoFrame import *
import pickle

class Welcome_Page:
	def __init__(self,root,client):
		self.root = root
		self.root.title('Githon Sign in')
		self.root.geometry('300x150')
		self.welcome_label = Label(self.root, text='Sign in to Github!',font=('Rouge',10))
		self.ghUsernameLabel = Label(self.root,text='Username')
		self.ghUsernameEntry = Entry(self.root, borderwidth= 2)
		self.ghPasswordLabel = Label(self.root,text='Password')
		self.ghPasswordEntry = Entry(self.root, borderwidth= 2)
		self.ghAccessTokenLabel = Label(self.root,text='Access Token')
		self.ghAccessTokenEntry = Entry(self.root, borderwidth= 2)
		self.var1 = IntVar()
		self.rememberMeCheckButton = Checkbutton(self.root, text="Remember me!", variable=self.var1)
		self.repoNB = tkrtk.Notebook(client)
		self.ghLoginButton = Button(self.root, text='Login!', command=lambda: login(self,client,self.ghUsernameEntry.get(),self.ghPasswordEntry.get(),self.root,self.repoNB,self.ghAccessTokenEntry.get()))


		#Checks if user has credentials stored
		picCredentials = os.path.expanduser('~/.config/Githon/Local/credentials.pickle')
		if os.path.exists(picCredentials):
			credentials = pickle.load(open(picCredentials,"rb"))
			self.ghUsernameEntry.insert(0, credentials['Username'])
			self.ghPasswordEntry.insert(0, credentials['Password'])
			self.ghAccessTokenEntry.insert(0, credentials['Access_Token'])
			self.rememberMeCheckButton.select()

		#Grid Assignements
		self.welcome_label.grid(column=1, sticky='w')
		self.ghUsernameLabel.grid(row=1)
		self.ghUsernameEntry.grid(row=1,column=1)
		self.ghPasswordLabel.grid(row=2)
		self.ghPasswordEntry.grid(row=2,column=1)
		self.ghAccessTokenLabel.grid(row=3)
		self.ghAccessTokenEntry.grid(row=3,column=1)
		self.ghLoginButton.grid(row=4,column=1)
		self.rememberMeCheckButton.grid(row=4)

def login(self,client,username,password,signInRoot,notebook = '',access_token = ''):
	self.root = client
	self.repoNb = notebook
	self.repoListBox =Listbox(self.root)
	counter = 0
	dic = {}
	g = Github(username,password)

	try:
		g.get_user()
	except:
		messagebox.showerror('Required Field', 'Please enter a valid decryption key')
		return
	try:
		self.homeSheet = tkrtk.Frame(self.repoNb)
		self.repoNb.add(self.homeSheet, text='Home')
		for repo in g.get_user().get_repos():
			tempSheet = RepoFrame(self.repoNb,self.root,repo,access_token,g)
		if self.var1.get() == 1:
			saveCredentials = {'Username':self.ghUsernameEntry.get(),'Password': self.ghPasswordEntry.get(),'Access_Token':self.ghAccessTokenEntry.get()}
			pickleDir = os.path.expanduser('~/.config/Githon/Local/credentials.pickle')
			pickle_out = open(pickleDir,"wb")
			pickle.dump(saveCredentials,pickle_out)
			pickle_out.close
		self.repoNb.grid(row=0)
		signInRoot.destroy()
	except:
		messagebox.showerror('Required Field', 'Invalid Login! \nPlease enter valid credentials')

