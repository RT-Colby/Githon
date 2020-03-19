from git import *
import os as os
from read_repo import *
from tkinter import *
import sys
import os
import webbrowser
from Initalize_Window import *
from Welcome_Page import *

master= Initalize_Window()



"""if __name__ == "__main__":

    repo_path = input('Enter your repo path\n')
    # Repo object used to programmatically interact with Git repositories
    repo = Repo(repo_path)
    print(Repo)
    # check that the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        #print("Remotes " + repo.remotes)
        # creates a list of commits then prints the first 5
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print('Could not load repository at {} :('.format(repo_path))	
"""