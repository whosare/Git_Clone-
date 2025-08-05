import os

def run(repo: str=None): #init function takes repository path as parameter
    if repo: #if we are provided a repo path
        cwd_path=repo
    else: #case if no path, meaning gitclone will be in current directory. 
        cwd_path=os.getcwd()    
    git_dir=os.path.join(cwd_path, ".gitclone")
    
    if os.path.exists(git_dir): #repo is the path of our directory
        print("The directory gitclone already exists")
        return
    else:
        os.makedirs(os.path.join(cwd_path, git_dir,"objects")) #creates objects subdirectory
        os.makedirs(os.path.join(cwd_path, git_dir,"refs")) #creates refs subdirectory
        
        file_path=os.path.join(git_dir, "HEAD")#file path to ..../HEAD
        with open(file_path, "w") as f: #open file for writing
            f.write("ref: refs/heads/main") #content of HEAD file
        print("GitClone successfully created.") #checker to make sure
        index_path=os.path.join(git_dir, "index")
        with open(index_path, "w") as g:
            pass

    