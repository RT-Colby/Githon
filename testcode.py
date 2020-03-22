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
import  platform


"""
def readRepo(reponame,ghAcc,access_token = '',branch=''):
	g = ghAcc
	if platform.system == 'Linux':
	    repoDir = os.path.expanduser('~/Repositories/')
	    #Checks if the Repositories Directory exists
	    if os.path.isdir(repoDir):
	    	#if repo exists create folder and clone it 
	        for repo in g.get_user().get_repos():
	            os.mkdir(repoDir + repo.name)
	            if repo.private:
	            	#Clones the repo using the access token
	                privUrl = formatUrl(repo.clone_url,access_token)
	               	Repo.clone_from(privUrl, repoDir + repo.name)
	            else:
	                Repo.clone_from(repo.clone_url, repoDir + repo.name )        
	    else:
	        for repo in g.get_user().get_repos():
	            os.makedirs(repoDir + repo.name)
	            if repo.private:
	            	#Clones the repo using the access token
	                privUrl = formatUrl(repo.clone_url,access_token)
	               	Repo.clone_from(privUrl, repoDir + repo.name)
	            else:
	                Repo.clone_from(repo.clone_url, repoDir + repo.name )   
	else:
	    #User is on windows
	    print('Not Implemented')
"""
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
	    		Repo.clone_from(repo.clone_url, repoDir + repo.name)
	else:
		print('Windows implemntation not done ')



for repo in g.get_user().get_repos():
    readRepo(repo,g,'42d9e665ee8b073088ffa76c98c157bac9c18e04')
    











    
"""
for repo in g.get_user().get_repos():
    privUrl = formatUrl(repo.clone_url,'2274ba30d60b953b2c826320f5408fd8fc3a4d81')
    print(privUrl)

url = 'https://github.com/ColbyFr/TestForDoc.git'
access_token = '4f5d27b90c78eb3a6be131b19f8be67cc7e739f4'
privUrl = formatUrl(url, access_token)
Repo.clone_from(privUrl,'/home/colby/Repositories/TestForDoc')
"""