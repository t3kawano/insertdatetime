#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:08:42 2023

@author: tk
"""

# 231216
# insert date, modified date to .md files for evernote derived obsidian files
# started from codes suggested by the google bard. It is not usable as it is
# but can be used to grasp what kind of functions are needed.

import os
import sys
import platform
import time
import datetime
import tkinter as tk
import tkinter.filedialog


def get_fileslist(directory):
    #directory = get_directory()
    fileslist = os.listdir(directory)
    print(fileslist)
    return fileslist


def get_file_creation_datetime(pathtoafile):
    if os.path.isfile(pathtoafile):
        #https://note.nkmk.me/python-os-stat-file-timestamp/
        #platform dependent codes
        if platform.system() == 'Windows':
            #return os.path.getctime(path_to_file)
            return datetime.datetime.fromtimestamp(os.stat(pathtoafile).st_ctime)            
        else:
            stat = os.stat(pathtoafile)
            try:
                #mac Darwin
                return datetime.datetime.fromtimestamp(os.stat(pathtoafile).st_birthtime)
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                #return stat.st_mtime    
                #as commented on the ref site, it is better to crealy say not available.
                return None      
    return None

def get_file_modified_datetime(pathtoafile):
    if os.path.isfile(pathtoafile):
        return datetime.datetime.fromtimestamp(os.stat(pathtoafile).st_mtime)
    return None

def insert_str_toafile(pathtoafile, string, position):
    if string is not None:
        if os.path.isfile(pathtoafile):
            # r+ read write mode, 
            #encoding="utf-8" required. otherwide cause error
            with open(pathtoafile, "r+", encoding="utf-8") as f:
                # keep file contents
                content = f.read()
                # seek position as top of file
                #f.seek(0)
                f.seek(position)
                # insert a line
                f.write(string + content)



#==============================================
#if this file is not impored from other modules
#if __name__ == "__main__":
linesep = os.linesep


root = tk.Tk()
root.withdraw()
#return os.path.normpath(tk.filedialog.askdirectory())
directory = os.path.normpath(tk.filedialog.askdirectory())
#tk.destroy()
print(directory)
#idir = directory

flist = get_fileslist(directory) 

for afile in flist:
    print(afile)
    pathtoafile= os.path.join(directory, afile)
    if os.path.isfile(pathtoafile):
        creationtime = get_file_creation_datetime(pathtoafile)
        modifiedtime = get_file_modified_datetime(pathtoafile)
        dt = "---"+linesep+ \
            f"creationtime: {creationtime: %Y-%m-%d %H:%M:%S.%f}"+linesep+ \
            f"modifiedtime: {modifiedtime: %Y-%m-%d %H:%M:%S.%f}"+linesep+\
            "---"+linesep
            
        print(dt)
        #print("---")
        #print("datetime: "+str(creationtime))
        #print("datemodified: "+str(modifiedtime))
        #print("---")
        insert_str_toafile(pathtoafile, dt, 0)
    else:
        print("not a file")
    

sys.exit()


#-------------------------------------------

dt = "---\n"\
    f"creationtime: {creationtime: %Y-%m-%d %H:%M:%S.%f}\n"\
    f"modifiedtime: {modifiedtime: %Y-%m-%d %H:%M:%S.%f}\n"\
    "---\n"
print(dt)

str(creationtime)


insert_str_toafile(pathtoafile, dt, 0)

    

os.name


os.linesep    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
