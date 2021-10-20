import os
import shutil
import time

path = input("Path of the Folder to be monitered : ")
ctime = os.stat(path).st_ctime
Days = input("Enter the number of days to delete : ")

Days = time.time()
if os.path.exists(path) :
    os.walk(path)
    path = path + "/"
else :
    print("Path not found")


if ctime > Days :
    os.remove(path)
    shutil.rmtree()

