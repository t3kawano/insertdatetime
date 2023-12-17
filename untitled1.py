#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:08:42 2023

@author: tk
"""

#insert date, modified date to .md files for evernote erived obsidian files
# asked google bard for such code. 
# based on that, modified.

import os
import system
import time
import datetime


def get_file_datetime(filename):
    if os.path.isfile(filename):
        return datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    return None

def write_file_datetime(filename):
    datetime = get_file_datetime(filename)
    if datetime is not None:
        with open(filename, "a") as f:
            f.write("# 作成日時: " + datetime.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("# 更新日時: " + datetime.strftime("%Y-%m-%d %H:%M:%S") + "\n")


#if this file is not impored from other modules
if __name__ == "__main__":
    filename = "sample.md"
    write_file_datetime(filename)
