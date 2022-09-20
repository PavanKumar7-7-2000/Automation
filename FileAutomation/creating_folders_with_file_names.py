import os

def CreatingFolders(path):    
    files = os.listdir(path)
    for file_name in files:
        file_path = os.path.join(path,file_name)
        dir_path = file_path[:-4]
        if not os.path.isdir(file_path):
            print(dir_path)
            isExist = os.path.exists(dir_path)
            if not isExist:
                os.makedirs(dir_path)

            
           
            
path = "E:/videos"
CreatingFolders(path)