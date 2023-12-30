import git

def commit_and_push(repo_path, commit_message, remote_name='origin', branch_name='main'):

    repo = git.Repo(search_parent_directories=True)
    repo_path = repo.working_tree_dir

    repo = git.Repo(repo_path)

    # Add changes
    repo.index.add('*')

    # Commit changes
    repo.index.commit("commit tst")

    # Push changes to the remote repository
    origin = repo.remotes[remote_name]
    origin.push(branch_name)

if __name__ == "__main__":
    # Replace these values with your repository information
    repository_path = '/path/to/your/repository'
    commit_message = 'Your commit message'

    commit_and_push(repository_path, commit_message)


