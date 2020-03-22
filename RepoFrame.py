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


class RepoFrame:
	def __init__(self,notebook,client,repo,access_token,ghAcc):
		self.testFrame = tkrtk.Frame(notebook, width=100)
		self.CloneRepoButton = Button(self.testFrame, text='clone!', command=lambda:readRepo(self.CloneRepoButton,repo,ghAcc,access_token))
		self.CloneRepoButton.grid()
		checkRepo_exist(repo,self.CloneRepoButton)
		notebook.add(self.testFrame, text=repo.name, )





