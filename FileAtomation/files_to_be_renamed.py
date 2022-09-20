import re
import os

def FilesToBeRenamed(path):      

    files_in_correct_format = 0

    files = os.listdir(path)

    files_to_be_renamed =[]

    for i in files:
        match = re.search(r"[0-9][0-9][0-9].day-[0-9][0-9][0-9]-lecture-[0-9][0-9][0-9].mp4", i)

        if match == None:

            files_to_be_renamed.append(i)

        else:

            files_in_correct_format+=1

    return files_to_be_renamed,files_in_correct_format




if __name__ == "__main__" :

    path = "E:/videos/computernetworking"

    files_to_be_renamed,files_in_correct_format = FilesToBeRenamed(path)

    for i in files_to_be_renamed:

        print(i)
        
    print(files_in_correct_format)