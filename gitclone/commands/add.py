import os
from ..utils.hash import hash_object

#This funciton assumes you are inside the directory where file_path is
def run(file_path: str):
    cwd_path=os.getcwd() #current home directory
    git_path=os.path.join(cwd_path, ".gitclone") #home_dir/.gitclone if exists
    if not os.path.exists(git_path):
        print("Need a git repository")
        return
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read() #converted file data to binary
            blob_hash=hash_object(binary_data, obj_type= "blob", write=True) #object is hashed
            #Unsure where to go from here?
            index_path=os.path.join(git_path, "index") #index path
            with open(index_path, 'a') as i_file:
                i_file.write(f"{blob_hash} {file_path}")
    
    except FileNotFoundError:
       print("Error: The file was not found.")
