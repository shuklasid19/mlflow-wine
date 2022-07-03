import os

dirs  = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    """
    iterate over all directories 
    #if the folder is not created then it will be created otherwise not
    we want to keep gitfile in each folders so it willbe created too

    """
    
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


#gitignore ignores files that we dont wanna push to github repo 
#we use it to not push files
#src/__init__.py will be used as package inside source folder to make
#source as a python package ---- src
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]

for file_ in files:
    """it will iterate and create templates 
    we wont be writing anything so we will use pass
    """
    with open(file_, "w") as f:
        pass