import os
from random import sample
import time
import shutil


path = "E:/other/Epsilon_Ai/lecture_8/Project 1 - Thanos/Project 1 - Thanos/universe" # path of file do you want to delete
os.chdir(path)                                                                        # change the defult path to the file 

def thanos_remove(path = path):                   # thanos function ' remove files '
    n = [ i for i in os.listdir()]
    half = len(n) // 2
    print("The name of the deleted file is :")
    for item in sample(n, half):
        
        print(item)
        os.remove(item)
        time.sleep(1)
        
        
src = "E:/other/Epsilon_Ai/lecture_8/Project 1 - Thanos/Project 1 - Thanos/backup"    # path of the file do you want to backup
dest = "E:/other/Epsilon_Ai/lecture_8/Project 1 - Thanos/Project 1 - Thanos/backup_2" # path of the destination backup file

def thanos_backup(src = src, dest = dest):          # backup function
    destination = shutil.copytree(src, dest) 
    return (f"the backup file is : {destination}")





thanos_backup()


thanos_remove()