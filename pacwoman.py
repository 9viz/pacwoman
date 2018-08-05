#!/usr/bin/python3
# Made by Th3-Hum4n in Github https://github.com/Th3-Hum4n
# Licensed under GPL v3. Feel free to edit it in the name of FREEDDOOOMM!

import subprocess
import urllib.request, urllib.error
import argparse
import shutil
import tarfile
import os

#import files
import configuration
import error_insults
import search

#get username
#calling Popen twice to ensure that the username is written to file. This is a workaround and if a better solution is know, please pull request.
subprocess.Popen("echo $USER > /tmp/username", shell=True)
subprocess.Popen("echo $USER > /tmp/username", shell=True)
with open("/tmp/username", "r") as username_file:
    for line in username_file:
        username = line

#get current directory
directory = os.getcwd()

#terminate if the user is root
if username == "root\n" and configuration.root_execute == False:
    print("{0}error:{1} this program is not allowed to be launched as root!".format(configuration.color_error, configuration.color_normal))
    exit()

#url and tar file template
#package_name = ""
#url_package = "https://aur.archlinux.org/cgit/aur.git/snapshot/{}.tar.gz".format(package_name)
#tar_package = "{}.tar.gz".format(package_name)

#change all colors to empty strings if colored_output is set to False in configuration.py

if configuration.colored_output == False:
    #set everything to empty strings 
    configuration.color_normal = ""
    configuration.color_error = ""
    configuration.color_successful = ""
    configuration.color_progress = ""

def retrieve_file(package_name):
#retrieves file from the AUR and saves it to the current working dir 
    url_package = "https://aur.archlinux.org/cgit/aur.git/snapshot/{}.tar.gz".format(package_name)
    tar_package = "{}.tar.gz".format(package_name)
    try:
        with urllib.request.urlopen(url_package) as response, open(tar_package, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print ("{0}downloaded:{1} {2}.tar.gz has saved to {3}".format(configuration.color_successful, configuration.color_normal, package_name, directory))
    except urllib.error.HTTPError:
        if configuration.insults == True:
            error_insults.print_insult()
            exit()
        else:
            print ("{0}error:{1} target not found: {2}".format(configuration.color_error, configuration.color_normal, package_name))
            exit()
        
def extract_tar(package_name):
#extracts the downloaded tar and saves it in the cwd.
#deletes the downloaded tar to prevent duplicates and confusion.
    tar_package = "{}.tar.gz".format(package_name)
    tar = tarfile.open(tar_package, "r:gz")
    print ("{0}extracting downloaded tarball.".format(configuration.color_progress))
    tar.extractall()
    tar.close()
    print ("{0}extracted:{1} downloaded {2}.tar.gz has been extracted".format(configuration.color_successful, configuration.color_normal, package_name))
    try:
        subprocess.Popen("rm -rf {0}".format(tar_package), shell=True)
        print ("{0}removed: {1}tar package has been removed and the contents has been stored in {2}/{3}".format(configuration.color_progress, configuration.color_normal, directory, package_name))
    except:
        print ("{0}error:{1} can't remove downloaded tarball, please remove it manually").format(configuration.color_error, configuration.color_normal)

def cd_to_package_dir():
    cd_to_dir = input("do you want to cd into the package directory? (y/n) ")
    if cd_to_dir.lower() == "yes" or cd_to_dir.lower() == "y":
        subprocess.Popen("cd {0}".format(package_name), shell=True)
    elif cd_to_dir.lower() == "no" or cd_to_dir.lower() == "n":
        exit()
    else:
        print ("error: invalid input")

#make all the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-S", metavar='', help="download package from AUR", nargs='+', default=None)
parser.add_argument("-Syu", help="download all the AUR package user has", action = "store_true")
parser.add_argument("-s", metavar="", help="fetch data of the package using the AUR RPC interface", nargs="+")
args = parser.parse_args()
#end all arguments

if args.S: 
    package_list = args.S
    for package_name in package_list:
        retrieve_file(package_name)
        extract_tar(package_name)
        if configuration.cd_to_package == True:
            cd_to_package_dir()
elif args.Syu:
# places all the installed aur packages to a text file
# read from the text file and generate a list
    subprocess.Popen("pacman -Qqm >> ./packages.txt", shell=True)
    with open("packages.txt", "r") as packages:
        installed_packages = [package.strip() for package in packages]
    for package in installed_packages:
        package_name = package
        retrieve_file(package_name)
        extract_tar(package_name)
elif args.s:
    package_list = args.s
    for package_name in package_list:
        search.search(package_name)
else:
    print("{0}error:{1} no argument given. launch 'pacwoman -h' to know all the options available".format(configuration.color_error, configuration.color_normal))
