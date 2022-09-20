import os 
import shutil

def moveFilesToFolders(path):
    files = os.listdir(path)
    for file_name in files:
        file_path = os.path.join(path,file_name)
        dir_path = file_path[:-4].strip(" ")
        if not os.path.isdir(file_path):
            print(file_path +"-->"+ dir_path)
            if os.path.isdir(dir_path):
                dest = shutil.move(file_path, dir_path) 
            else:
                print("No Directory " + dir_path)



path = os.path.join("E:","videos")
moveFilesToFolders(path)