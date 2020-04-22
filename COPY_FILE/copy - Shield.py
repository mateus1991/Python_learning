from shutil import copyfile
import os
import time
import datetime

source1 ='C:/Users/mateu/AppData/Roaming/Ryujinx/bis/user/save/0000000000000002/0/main'
source2 ='C:/Users/mateu/AppData/Roaming/yuzu/nand/user/save/0000000000000000/7884BAA36538F4879424E5B603932BAD/01008DB008C2C000/main'

time1= round(os.stat(source1).st_mtime)
time2= round(os.stat(source2).st_mtime)

if time1>time2 :
    copyfile(source1, source2)
else: 
    copyfile(source2, source1)
