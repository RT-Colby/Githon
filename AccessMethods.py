from git import *
from github import Github
import os as os
from read_repo import *
from tkinter import *
import sys
import os
import webbrowser

def login(username,password):
	g = Github(username,password)
	for repo in g.get_user().get_repos():
		print(repo.name)
