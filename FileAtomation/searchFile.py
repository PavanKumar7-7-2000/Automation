from msilib.schema import Directory
import re
import os

def FileToSearch(path,n):    
    n+=1  
    files = os.listdir(path)
    for i in files:
        file_path = os.path.join(path,i)
        if os.path.isdir(file_path):
            #print("|"+"D :"+"-"*n + i)
            FileToSearch(file_path,n)
        else:
            if '.dat' in i:
                print(file_path)
            #print("|"+"-"*n + i)
path = "C:/Users/PavanKumar/Desktop/Hill_Climb_Racing_com.fingersoft.hillclimb"
FileToSearch(path,0)