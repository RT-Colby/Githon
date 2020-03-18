from git import *
import os as os
from read_repo import *


"""
class Main:
	def __init__(self):
		repo = Repo(self.rorepo.working_tree_dir, bare=True)
		assert  repo.bare
		repo.config_reader()
		with repo.config_wirter():
			pass
		assert not bare_repo_is_dirty()
		repo.untracked_files
"""
if __name__ == "__main__":
    repo_path = os.getenv('GIT_REPO_PATH')
    # Repo object used to programmatically interact with Git repositories
    repo = Repo(repo_path)
    # check that the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print('Could not load repository at {} :('.format(repo_path))	
