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


def formatUrl(pubUrl,access_token):
    splitUrl = pubUrl.split('/')
    x = ''
    x = splitUrl[0] + r'//' + access_token + ':x-oauth-basic@github.com/' + splitUrl[3] + '/' + splitUrl[4]
    return x

def readRepo(repo,ghAcc,access_token = '',branch=''):
	g = ghAcc
	if sys.platform == 'linux':
	    repoDir = os.path.expanduser('~/Repositories/')
	    #Checks if there is already a folder for the repo
	    if os.path.isdir(repoDir + repo.name) != True:
	    	#if the repo doesnt exsit, clone it 
	    	if repo.private:
	    		#Clones the repo using the access token
	    		privUrl = formatUrl(repo.clone_url,access_token)
	    		Repo.clone_from(privUrl, repoDir + repo.name)
	    	else:
	    		#Clones repo using http url
	    		Repo.clone_from(repo.clone_url, repoDir + repo.name)
	else:
		print('Windows implemntation not done ')


