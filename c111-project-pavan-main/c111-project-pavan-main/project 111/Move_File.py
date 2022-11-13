import os
import shutil

from_dir="C:/Users/lenovo/Downloads"
to_dir="C:/Users/lenovo/Documents"
x = os.listdir(from_dir)

for y in x :
    name,extension=os.path.splitext(y)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in[".txt",".doc",".docx","pdf"]:
        path1=from_dir+"/"+y
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+y
        if os.path.exists(path2):
            print("moving"+y+"..")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+y+"..")
            shutil.move(path1,path3)