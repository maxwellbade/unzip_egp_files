#!/usr/bin/env python
# coding: utf-8

#script 1
#extract single .egp file based on directory variable
zip_folder = r'folder/with/all/zip/files'
destination = r'destination/folder'
# pwd = '<YOUR_PASSWORD>'

with zipfile.ZipFile(zip_folder) as zf:
    zf.extractall(
        destination) #pwd=pwd.encode())

#script 2
#get files from directory based on list of extentsions
import os
import zipfile

#create directory and extension variables
rootdir = r'folder/with/all/zip/files'
destination = r'destination/folder'
extensions = ('.egp', '.sas', '.xml')

#loop through the directory/subdirectories and extract .egp files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext == '.egp': #change to other extension if necessary
            files = os.path.join(subdir, file)
            print(files)
            # pwd = '<YOUR_PASSWORD>' #insert password if directory is password protected

            with zipfile.ZipFile(files) as zf:
                zf.extractall(
                    destination) #pwd=pwd.encode())

#script 3
#list all files and folders in a specific folder and add them to a list
from os import listdir
from os.path import isfile, isdir, join

#get only files or only dirs
onlyfiles = [f for f in listdir(destination) if isfile(join(destination, f))]
onlydirs = [f for f in listdir(destination) if isdir(join(destination, f))]

print('All Files:')
for i in onlyfiles:
    print(i)
print('')
print('All Folders:')
for i in onlydirs:
    print(i)
