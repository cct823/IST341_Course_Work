#
# hw5pr1.py ~ file and recipe analysis
#
# Name(s):
#

import os
import os.path
import shutil

def count_txt_files( L ):
    """ count_txt_files takes in a list, L
        whose elements are (dirname, listOfSubdirs, listOfFilenames )
    """
    for element in L:
        dirname, LoD, LoF = element
        print("dirname is", dirname)
        subdir_count = len(LoD)
        file_count = len(LoF)
        print("  + it has", subdir_count, "subdirectories")
        print("  + and   ", file_count, "files")
    return 42  # this is not (yet) correct!

if True:
    """ run functions/code here... """
    L = list(os.walk("."))
    num_txt_files = count_txt_files( L )
    #print()
    #print("count_txt_files returned", num_txt_files, "files.")






#
# be sure your file runs from this location,
# relative to the "recipes" files and directories
#


