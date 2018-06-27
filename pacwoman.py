#!/usr/bin/env python3
# Made by Th3-Hum4n in Github https://github.com/Th3-Hum4n
# Licensed under GPL v3. Feel free to edit it in the name of FREEDDOOOMM!

import subprocess
import error_insults
import urllib.request
import argparse
import shutil
import tarfile
import os
import configuration
from random import randint

"""todo:
        find a way to input multiple packages at once. possibly using yaml(?)
"""
directory = os.getcwd()
package_name = ""
url_package = "https://aur.archlinux.org/cgit/aur.git/snapshot/{}.tar.gz".format(package_name)
tar_package = "{}.tar.gz".format(package_name)

#change all colors to white if colored_output is set to False in configuration.py. pass when colored_output is set to True

if configuration.colored_output == True:
    pass
elif configuration.colored_output == False:
    #set everything to white
    configuration.color_normal = "\033[0m"
    configuration.color_error = "\033[0m"
    configuration.color_successful = "\033[0m"
    configuration.color_progress = "\033[0m"
else:
    print ("you entered some gibberish in configuration.py")

def retrieve_file():
#retrieves file from the AUR and saves it in the user set download dir. or fall back to cwd if there's no config file
    try:
        with urllib.request.urlopen(url_package) as response, open(tar_package, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print ("{0}downloaded:{1} {2}.tar.gz has saved to {3}".format(configuration.color_successful, configuration.color_normal, package_name, directory))
    except:
        if configuration.insults == True:
            print(error_insults.error_insults[randint(0, len(error_insults.error_insults))])
            exit()
        elif configuration.insults == False:
            print ("{0}error:{1} target not found: {2}".format(configuration.color_error, configuration.color_normal, package_name))
            exit()
        else:
            print ("you entered some gibberish in configuration.py")

def extract_tar():
#extracts the downloaded tar and saves it in the cwd.
#deletes the downloaded tar to prevent duplicates and confusion.
    tar = tarfile.open(tar_package, "r:gz")
    print ("{0}extracting downloaded tarball.".format(configuration.color_progress))
    tar.extractall()
    tar.close()
    print ("{0}extracted:{1} downloaded {2}.tar.gz has been extracted".format(configuration.color_successful, configuration.color_normal, package_name))
    try:
        subprocess.Popen(["rm", "-r", "{}".format(tar_package)])
        print ("{0}removed: {1}tar package has been removed and the contents has been stored in {2}/{3}".format(configuration.color_progress, configuration.color_normal, directory, package_name))
    except:
        print ("{0}error:{1} can't remove downloaded tarbar, please remove it manually").format(configuration.color_error, configuration.color_normal)

def cd_to_package_dir():
    cd_to_dir = input("do you want to cd into the package directory? (y/n) ")
    if cd_to_dir.lower == "yes" or cd_to_dir.lower == "y":
        subprocess.Popen(["cd", "{}".format(package_name)])
    elif cd_to_dir.lower == "no" or cd_to_dir.lower == "n":
        exit()
    else:
        print ("error: invalid input")

#make all the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-S", help="download package from AUR")
parser.add_argument("-Syu", help="download all the AUR package user has", action = "store_true")
args = parser.parse_args()
#end all arguments

if args.S:
    package_name = args.S
    url_package = "https://aur.archlinux.org/cgit/aur.git/snapshot/{}.tar.gz".format(package_name)
    tar_package = "{}.tar.gz".format(package_name)
    retrieve_file()
    extract_tar()
    #cd_to_package_dir()
elif args.Syu:
# places all the installed aur packages to a text file
# read from the text file and generate a list
    subprocess.Popen("pacman -Qqm >> ./packages.txt", shell=True)
    with open("packages.txt", "r") as packages:
        installed_packages = [package.strip() for package in packages]
    for package in installed_packages:
        package_name = package
        url_package = "https://aur.archlinux.org/cgit/aur.git/snapshot/{}.tar.gz".format(package_name)
        tar_package = "{}.tar.gz".format(package_name)
        retrieve_file()
        extract_tar()

else:
    print("{0}error:{1} no argument given. launch 'pacwoman -h' to know all the options available").format(configuration.color_error, configuration.color_normal)
