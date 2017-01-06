# coding: utf-8

"""
Remove the files from folder
"""

import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

def removeFiles(directory):
    """ Remove the files from folder
        Also delete the folder
    """
    shutil.rmtree(directory, onerror=remove_readonly)


if __name__ == '__main__':
    directory = 'E:\\delete'
    try:
        removeFiles(directory)
    except Exception as e:
        print(type(e))
        print(e)
