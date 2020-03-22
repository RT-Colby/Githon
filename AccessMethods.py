from git import *
from github import Github
import os as os
from tkinter import *
import sys
import os
import webbrowser
import tkinter.ttk as tkrtk
from tkinter import messagebox
import platform
import pickle
import git



def formatUrl(pubUrl,access_token):
    splitUrl = pubUrl.split('/')
    access_token.replace(' ', '')
    x = ''
    x = splitUrl[0] + r'//' + str(access_token) + ':x-oauth-basic@github.com/' + splitUrl[3] + '/' + splitUrl[4]
    return x

def readRepo(cloneButton,repo,ghAcc,access_token = '',branch=''):
	g = ghAcc
	if sys.platform == 'linux':
	    repoDir = os.path.expanduser('~/Repositories/')
	    #Checks if there is already a folder for the repo
	    if os.path.isdir(repoDir + repo.name) != True:
	    	#if the repo doesnt exsit, clone it 
	    	if repo.private:
	    		if branch == '':
	    			#Clones the master branch of the repo using the access token
	    			privUrl = formatUrl(repo.clone_url,access_token)
	    			Repo.clone_from(privUrl, repoDir + repo.name,branch='master')
	    			cloneButton.grid_forget()
	    		else:
	    			#Clones a specific branch of the repo using the access token
	    			privUrl = formatUrl(repo.clone_url,access_token)
	    			Repo.clone_from(privUrl, repoDir + repo.name,branch=branch)
	    			cloneButton.grid_forget()
	    	else:
	    		#Clones using http
	    		if branch == '':
	    			#Clones the master branch of the repo 
	    			Repo.clone_from(repo.clone_url, repoDir + repo.name, branch='master')
	    			cloneButton.grid_forget()
	    		else:
	    			#Clones a specific branch of the repo
	    			Repo.clone_from(privUrl, repoDir + repo.name,branch=branch)
	    			cloneButton.grid_forget()

	else:
		print('Windows implemntation not done ')

def checkRepo_exist(repo,button):
	if sys.platform == 'linux':
		repoDir = os.path.expanduser('~/Repositories/')
		if os.path.isdir(repoDir + repo.name) == True:
			button.grid_forget()
	else:
		print('Windows implemntation not done')


def commitChanges(self,repoObj,commitMessage,ghAcc,branch ='',access_token=''):
	if sys.platform == 'linux':
		repoDir = os.path.expanduser('~/Repositories/' + repoObj.name)
		user = ghAcc.get_user()
		repo = git.Repo(repoDir)
		repo.git.add(repoDir + r'/.')
		repo.git.commit('-m', commitMessage, author= user.email)
		return true
	else:
		print('Windows implemntation not done')


