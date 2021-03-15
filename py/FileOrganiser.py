import os
import shutil
path=input("Enter the name of the directory to be sorted. ")
listOfFiles=os.listdir(path)
for file in listOfFiles:
    name,pxt=os.path.splitext(file)
    pxt=pxt[1:]
    if pxt=='':
        continue
    if os.path.exists(path+'/'+pxt):
        shutil.move(path+'/'+file,path+'/'+pxt+'/'+file)
    else:
        os.makedirs(path+'/'+pxt)
        shutil.move(path+'/'+file,path+'/'+pxt+'/'+file)