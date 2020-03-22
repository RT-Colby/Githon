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

class RepoFrame:
	def __init__(self,notebook,client,repo,access_token,ghAcc):
		#Page Setup
		self.frame = tkrtk.Frame(notebook, width=500, height=900)
		self.CloneRepoButton = Button(self.frame, text='clone!', command=lambda:readRepo(self.CloneRepoButton,repo,ghAcc,access_token))
		self.ChangesListBoxLabel = Label(self.frame, text='List of files that have been Changed')


		#Gets Changed Files for commits
		self.ChangesListBox = Listbox(self.frame,width=50)
		repoDir = os.path.expanduser('~/Repositories/' + repo.name)
		pyRepo =git.Repo(repoDir)
		changed_files = pyRepo.git.diff(None,name_only=True)
		counter = 0
		for f in changed_files.split('\n'):
			self.ChangesListBox.insert(counter,f)

		#Grid assignments
		self.frame.grid_columnconfigure(0,minsize=180 )
		self.ChangesListBoxLabel.grid(row=0)
		self.CloneRepoButton.grid(row=1)
		self.ChangesListBox.grid()
		checkRepo_exist(repo,self.CloneRepoButton)
		notebook.add(self.frame, text=repo.name)






