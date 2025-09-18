#----- Module ------
# Module: a python file that we can import into our current python file

  # We don't have to copy any functions or any variables or anything over into this file, yet we are albe to use all the stuff in the python file imported.
  # Module pool: http://doc.python.org/3/py-modindex.html ; Search key word " list of python modules" - built in python files that we can access directly.
               # Above python variables and functions - list on the official python docs
               # There are also third pary python module: key word "python module for doing X"
  # Import a python file to access its variables and functions

import Useful_Tools

print(Useful_Tools.roll_dice(10))

  # Q: where are the modules files in the pool stored? http://doc.python.org/3/py-modindex.html
    # A: There are two types of module: 1. Built in modules - they are just built into Python language
    #                                   2. External modules - same folder we install python in our computer - In pycharm, they can be found in External Libraries - Lib - on the left under Project file folder
    #                                      when we click on the detail page in the link, we will see "Source code: Lib/base64.py"; if it doesn't say the source it is built in python
#   Q: What about using modules other people have written
    # A: Install third pary modules 1. Find the one you want to use. e.g. python-docx - google it  - this module use python to create word documents
    #                               2. In the installation instruction: pip install xxx


#----- pip ------
# pip: it's referred to as a package manager - allow us to install, manage update and uninstall different python modules.
   # The pip is essentially a program. We can use it to install python modules. It is pre-installed in python three.
   # To use pip to install third party module: 1. Open up command prompts (Windows： CMD) / terminal (Mac)
   #                                           2. (Windows CMD type in）  "pip --version"  -  we want to see if we have pip installed and the version
   #                                           3. (Windows CMD type in）  "pip install xxx(name of the third pary module)"
   #                                           4.  Installation finished.
   # When we install a third party module, it's going to get put inside the lib folder - special folder called "site-packages"
         #  If we want to use those inside our program, we  can refer to the name of the module - the sub-file name in the "site-packages" folder.

import google
google.

   # Remove the module: (Windows CMD type in）  "pip uninstall xxx(module name)"
       #  The sub-folder in "site-packages", same as the module, disappear


