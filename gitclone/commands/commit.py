import os
from gitclone.objects.tree import write_tree

def run(message: str):
    cwd_path=os.getcwd() #get current dir
    dir_path=os.path.join(cwd_path, ".gitclone") #path of cwd/gitclone

    if not os.path.exists(os.path.join(dir_path, "index")):
        print("Nothing to commit")
        return
    
    index_path=os.path.join(dir_path, "index")
    
    entries = []
    with open(index_path, "r") as f:
        for line in f:
            blob_hash, file_path = line.strip().split(" ", 1)
            entries.append((file_path, blob_hash))
            print(file_path, blob_hash)
            
        tree_hash = write_tree(entries)
        print(f"Tree created: {tree_hash}")