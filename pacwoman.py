#!/usr/bin/python3
# Made by Th3-Hum4n in Github https://github.com/Th3-Hum4n
# Licensed under GPL v3. Feel free to edit it in the name of FREEDDOOOMM!

import subprocess
import urllib.request, urllib.error
import argparse
import shutil
import tarfile
import os
import sys
import json
from getpass import getuser

# import files
import configuration
import error_insults
import search

def retrieve_file(package_name):
    #retrieves file from the AUR and saves it to the current working dir 
    url_package = "https://aur.archlinux.org/cgit/aur.git/snapshot/" + \
        package_name + ".tar.gz"
    tar_package = package_name + ".tar.gz"
    try:
        with urllib.request.urlopen(url_package) as response, open(tar_package, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print ("{0}downloaded:{1} {2}.tar.gz has saved to {3}"\
                .format(configuration.color_successful, configuration.color_normal, package_name, directory))
    except urllib.error.HTTPError:
        if configuration.insults:
            error_insults.print_insult()
            sys.exit()
        else:
            print ("{0}error:{1} target not found: {2}"\
                    .format(configuration.color_error, configuration.color_normal, package_name))
            sys.exit()
    except KeyboardInterrupt:
        sys.exit()
        
def extract_tar(package_name):
    #extracts the downloaded tar and saves it in the cwd.
    #deletes the downloaded tar to prevent duplicates and confusion.
    tar_package = package_name + ".tar.gz"
    tar = tarfile.open(tar_package, "r:gz")

    print(configuration.color_progress + "extracting downloaded tarball")

    tar.extractall()
    tar.close()

    print(configuration.color_successful + "extracted:" + \
        configuration.color_normal + " downloaded " + package_name + \
        ".tar.gz has been extracted")

    try:
        rm_tar = subprocess.Popen("rm -rf {0}".format(tar_package), shell=True)
        rm_tar.wait()
        print(configuration.color_progress + "removed:" + \
            configuration.color_normal + " tar package has been removed" + \
            " and the contents have been stored in %s/%s" % (directory,
                package_name))
    except:
        print(configuration.color_error + "error:" + \
            configuration.color_normal + " can't remove downloaded tarball" + \
            ", please remove it manually")
        
def cd_to_package_dir():
    cd_to_dir = input("do you want to cd into the package directory? (y/n) ")
    cd_to_dir = cd_to_dir.lower()
    if cd_to_dir in ["yes", "y"]:
        subprocess.Popen("cd " + package_name, shell=True)
    else:
        sys.exit()

# update all packages which are not up-to-date
def smart_update_package():
    # init count of packages to be updated
    package_update_count = 0

    # get packages installed with their version number
    get_package_with_ver = subprocess.Popen("pacman -Qm > ./ver_packages.txt",
                                            shell=True)
    get_package_with_ver.wait()

    with open(directory + "/ver_packages.txt", "r") as packages:
        installed_packages_ver = [package.strip() for package in packages]
    rm_file = subprocess.Popen("rm -rf ./ver_packages.txt", shell=True)
    rm_file.wait()
    
    # get packages installed without version number
    get_package = subprocess.Popen("pacman -Qqm > ./packages.txt", shell=True)
    get_package.wait()

    with open(directory + "/packages.txt", "r") as packages:
        installed_packages = [package.strip() for package in packages]
    rm_file = subprocess.Popen("rm -rf ./packages.txt", shell=True)
    rm_file.wait()
   
    # really loopy way to download packages. explanation below
    # check if the package with the version in the user system is equal to the package with the version available in the aur
    # if it is, update; else, break the loop 
    for package_name in installed_packages:
        package_data = search.search(package_name, "name")
        for result in package_data["results"]:
            # check if the package name is exactly the same. lemonbar matches only to lemonbar and not lemonbar-xft-git
            if result["Name"] == package_name: 
                aur_package_with_ver = "%s %s" % (result["Name"],
                    result["Version"]) 
                for package_with_ver in installed_packages_ver:
                    # if the version of the package installed in the system is not equal to the version in the aur, update
                    if package_with_ver != aur_package_with_ver: 
                        retrieve_file(package_name)
                        extract_tar(package_name)
                        package_update_count += 1
                        # exit out of loop after we download package 
                        break

    if package_update_count == 0:
        print("all packages are up to date")


if __name__ == '__main__':
    error = lambda text: configuration.color_error + "error:" + \
        configuration.color_normal + " " + text

    #get username
    if getuser() == "root" and not configuration.root_execute:
        print(error("this program is not allowed to be used as the root user"))
        exit(1)

    #get current directory
    directory = os.getcwd()

    #change all colors to empty strings if colored_output is set to False in configuration.py
    if not configuration.colored_output:
        configuration.color_normal = ""
        configuration.color_error = ""
        configuration.color_successful = ""
        configuration.color_progress = ""


    #make all the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-S", metavar="", help="download package from AUR", nargs="+", default=None)
    parser.add_argument("-Syu", help="download all the AUR package user has", action = "store_true")
    parser.add_argument("-s", metavar="", help="fetch data of the package using the AUR RPC interface", nargs="+")
    parser.add_argument("-c", help="set the config file directory", metavar=" ")
    args = parser.parse_args()
    #end all arguments

    if args.S: 
        package_list = args.S
        for package_name in package_list:
            retrieve_file(package_name)
            extract_tar(package_name)
            if configuration.cd_to_package:
                cd_to_package_dir()
    elif args.Syu:
        # read comments in the function to understand how it works.
        smart_update_package()
    elif args.s:
        package_list = args.s
        for package_name in package_list:
            search_data = search.search(package_name, configuration.search_type)
            search.pretty_print_json(search_data)
    elif args.c:
        if os.path.isfile(args.c): 
            configuration.writeConfigDir(os.path.abspath(args.c))
        else:
            print(error("file does not exists"))
    else:
        print(error("no argument given. launch 'pacmwoman -h' for the options available."))
