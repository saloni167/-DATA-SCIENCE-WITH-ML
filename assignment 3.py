import os
import shutil
os.chdir(r"C:\Users\Dell\Desktop\testing")
Destination_File = r"C:\Users\Dell\Desktop\jodhpur\images_files"
Destination_File1 = r"C:\Users\Dell\Desktop\jodhpur\images_files"
Destination_File2 = r"C:\Users\Dell\Desktop\jodhpur\text_files"
lst = os.listdir()
for File in lst:
    if File.endswith('.png') or File.endswith('.jpg'):
        shutil.move(File, Destination_File)
    elif File.endswith('.txt'):
        shutil.move(File, Destination_File1)
    elif File.endswith('.pdf'):
        shutil.move(File, Destination_File2)