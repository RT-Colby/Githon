from os import *
from git import *

COMMITS_TO_PRINT = 5

""" Prints
    the commit summary
    author name
    author email
    commit date and time
    count and update size
"""


def print_Commit(commit):
	print('----')
	print(str(commit.hexsha))
	print("\"{}\" by {} ({})".format(commit.summary,commit.author.name,commit.author.email))
	print(str(commit.authored_datetime))
	print(str("Count: {} and size: {}".format(commit.count(),commit.size)))

def print_repository(repo):
	print('Repo description: {}'.format(repo.description))
	print('Repo active branch is {}'.format(repo.active_branch)
	for remote in repo.remotes:
		print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
		print('Last commit for repo is {}.'.format(str(repo.head.comit.hexsha)))

