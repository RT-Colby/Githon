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

for repo in g.get_user().get_repos():
    privUrl = formatUrl(repo.clone_url,'2274ba30d60b953b2c826320f5408fd8fc3a4d81')
    print(privUrl)

url = 'https://github.com/ColbyFr/TestForDoc.git'
access_token = '4f5d27b90c78eb3a6be131b19f8be67cc7e739f4'
privUrl = formatUrl(url, access_token)
Repo.clone_from(privUrl,'/home/colby/Repositories/TestForDoc')