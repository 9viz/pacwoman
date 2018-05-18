import subprocess
import urllib.request
import argparse
import shutil
import tarfile
import os

"""todo:
    make arguments to download instead of input
    download all the AUR packages user when evoked with -Syu
    make a config file where user can enable colored output

"""
#make all the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-S", help="download package from AUR")
#parser.add_argument("-Syu", help="download all the AUR package user has")
args = parser.parse_args()
#end all arguments
directory = os.getcwd()
package_name = args.S
url_package = "https://aur.archlinux.org/cgit/aur.git/snapshot/{}.tar.gz".format(package_name)
tar_package = "{}.tar.gz".format(package_name)
def retrieve_file():
#retrieves file from the AUR and saves it in the user set download dir. or fall back to cwd if there's no config file
    try:
        with urllib.request.urlopen(url_package) as response, open(tar_package, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print ("downloaded: {0}.tar.gz has saved to {1}".format(package_name, directory))
    except:
        print ("error: target not found: {0}".format(package_name))
        exit()
def extract_tar():
#extracts the downloaded tar and saves it in the cwd.
#deletes the downloaded tar to prevent duplicates and confusion.
    tar = tarfile.open(tar_package, "r:gz")
    print ("extracting downloaded tarball.")
    tar.extractall()
    tar.close()
    print ("extracted: downloaded {0}.tar.gz has been extracted".format(package_name))
    try:
        subprocess.Popen(["rm", "-r", "{}".format(tar_package)])
        print ("removed: tar package has been removed and the contents has been stored in {0}/{1}".format(directory, package_name))
    except:
        print ("error: can't remove downloaded tarbar, please remove it manually")

def cd_to_package_dir():
    cd_to_dir = input("do you want to cd into the package directory? (y/n) ")
    if cd_to_dir.lower == "yes" or cd_to_dir.lower == "y":
        subprocess.Popen(["cd", "{}".format(package_name)])
    elif cd_to_dir.lower == "no" or cd_to_dir.lower == "n":
        exit()
    else:
        print ("error: invalid input")
retrieve_file()
extract_tar()
#cd_to_package_dir()
