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
		pyRepo = git.Repo(repoDir)
		changed_files = pyRepo.git.diff(None,name_only=True)
		counter = 0
		branches = repo.get_branches()
		branch = []

		#Crets a list of each repo branchs
		self.branchSelection = StringVar(self.frame)
		for x in branches:
			branch.append(x.name)
		self.branchSelection.set(branch[0])
		self.branchBox=OptionMenu(self.frame,self.branchSelection,*branch)



		#Grid assignments
		self.ChangesListBoxLabel.grid(row=0)
		self.CloneRepoButton.grid(row=1)
		self.branchBox.grid()
		self.ChangesListBox.grid()
		checkRepo_exist(repo,self.CloneRepoButton)
		notebook.add(self.frame, text=repo.name)

		#looks for changed files, then adds commit/push buttons
		if changed_files == '':
			self.ChangesListBox.insert(0,'No Changes Detected')
		else:
			for f in changed_files.split('\n'):
				self.ChangesListBox.insert(counter,f)
			self.commitLabel = Label(self.frame, text='Enter your commit message').grid()
			self.CommitMessage = Entry(self.frame)
			self.CommitMessage.grid()
			self.CommitButton = Button(self.frame, text='Commit Changes',command=lambda: commitChanges(self,repo,self.CommitMessage.get(),ghAcc,branch=self.branchSelection.get())).grid()






