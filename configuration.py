#!/usr/bin/python3

# if you want to disable error insults, then set it to "True"
# default is "False"
insults = False 

# set it to "True" if you want colored output
# default is "False"
colored_output = False 

# colors declaration in ANSI code.
color_normal = "\033[0m" # default: white
color_error = "\033[1;31m" # default: red
color_successful = "\033[1;32m" # default: green
color_progress = "\033[33m" # default: yellow
color_search_heading = "\033[34m" # default: blue

# set it to "True", if you want to cd into the package directory
# default is "False"
cd_to_package = False

# set it to "True" if you want to use this script as a root user
# default is "False"
root_execute = False

# sets the option you can search by.
# available options are name, name-desc, maintainer, none
# name only searches the package's name
# name-desc searches the package's name and its description
# maintainer searches the maintainer's name
# none searches for everything
# NOTE: It is important that you don't assign an invalid value to the variable. If you do, search simply won't work!
# default is name
search_type = "name" 
