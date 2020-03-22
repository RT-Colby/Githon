from git import *
from github import Github
import os as os
from read_repo import *
from tkinter import *
import sys
import os
import webbrowser
import tkinter.ttk as tkrtk
from tkinter import messagebox
import platform

def login(self,root,notebook,username,password,signInRoot):
	self.root = root
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
		dic['Home'] = self.homeSheet
		for repo in g.get_user().get_repos():
			self.tempSheet = tkrtk.Frame(self.repoNb)
			dic[repo.name] = self.tempSheet
			counter += 1
		for frame in dic:
			self.repoNb.add(dic[frame], text=frame)
		self.repoNb.grid(row=0)
		signInRoot.destroy()
	except:
		messagebox.showerror('Required Field', 'Invalid Login! \nPlease enter valid credentials')

def readRepo(reponame,ghAcc,access_token = '',branch=''):
	g = ghAcc
	if platform.system == 'Linux':
	    repoDir = os.path.expanduser('~/Repositores/')
	    #Checks if the Repositories Directory exists
	    if os.path.isdir(repoDir):
	        for repo in g.get_user().get_repos():
	            os.mkdir(path + repo.name)
	            if repo.private:
	                print('NI')
	            else:
	                Repo.clone_from(repo.clone_url, path + repo.name )        
	    else:
	        for repo in g.get_user().get_repos():
	            os.makedirs(path + repo.name)
	            Repo.clone_from(repo.clone_url, path + repo.name ) 
	else:
	    #User is on windows
	    print('Not Implemented')

def formatUrl(pubUrl,access_token):
    splitUrl = pubUrl.split('/')
    x = ''
    x = splitUrl[0] + r'//' + access_token + ':x-oauth-basic@github.com/' + splitUrl[3] + '/' + splitUrl[4]
    return x



