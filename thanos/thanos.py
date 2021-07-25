import os
from random import sample


def thanos(path) :
    
    # path and file direction

    cd = os.chdir(path)
    Universe = os.listdir()
    
    # number of files in folder

    folder = [i for i in Universe]

    enum = list( enumerate(folder) )

    half_num =int(len(folder)/ 2 )

    # make object from .... to use

    remove_file = os.remove
    
    for file in sample( folder, half_num) :

        remove_file(file)
        

# ex : as

thanos("C:\\Users\\Mora\\Desktop\\thanos\\Universe") 