import os
from collections import defaultdict
from files_to_be_renamed import FilesToBeRenamed
from find_the_match import Find_The_Match

def RenameFileByPattern(files,path):

    d = defaultdict(int)

    files_to_be_renamed,files_in_correct_format = FilesToBeRenamed(path)

    for i in files_to_be_renamed:

        file_path = os.path.join(path, i)

        start,end = Find_The_Match('day-[0-9]*', i)

        d[i[start:end]]+=1
        
        files_in_correct_format+=1

        seq_no = seq_no_file(files_in_correct_format)

        day_no = day_no_file(i,start,end)

        new_name =seq_no + "." + "day-" + day_no + "-lecture-" + "00" + str(d[i[start:end]]) +".mp4"

        print(i)

        print("----"+new_name)

        #new_file_path = os.path.join(path,new_name)

        #os.rename(file_path, new_file_path)




def seq_no_file( files_in_correct_format, no_of_digits_in_seq_no = 3 ):

    no_of_zeroes_in_seq_no = no_of_digits_in_seq_no - len(str(files_in_correct_format))

    seq_no = "0"*no_of_zeroes_in_seq_no + str(files_in_correct_format)

    return seq_no



def day_no_file(i, start, end, no_of_digits_in_day_no = 3):

    no_of_zeroes_in_day_no = no_of_digits_in_day_no-len(i[start+4:end])

    day_no = "0"*no_of_zeroes_in_day_no + i[start+4:end]

    return day_no





if __name__ == "__main__" :

    path = "E:/videos/computernetworking"

    files = os.listdir(path)

    RenameFileByPattern(files,path)
