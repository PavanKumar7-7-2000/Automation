import os
import time
 
# Path to the file/directory
path = os.getcwd()

files = os.listdir(path)

for i in files:

    file_path=os.path.join(path, i)

    ti_c = os.path.getctime(file_path)

    c_ti = time.ctime(ti_c)

    print(ti_c,c_ti)

 
# Both the variables would contain time
# elapsed since EPOCH in float

# ti_c = os.path.getctime(path)
# ti_m = os.path.getmtime(path)
 
# # Converting the time in seconds to a timestamp
# c_ti = time.ctime(ti_c)
# m_ti = time.ctime(ti_m)
 
