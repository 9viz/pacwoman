#!/usr/bin/python3
#Get package's info in json using the AUR's RPC interface
#Accompanies pacwoman.py

import json
import urllib.request

#import files
import configuration

#set search's heading to an empty str if colored output is set to False
if configuration.colored_output == False:
    configuration.color_search_heading = ""

def pretty_print_json(json_data):
    nth_iteration = 0
    num_results = len(json_data["results"])
    print("{0}Results:{1} {2}\n".format(configuration.color_search_heading, configuration.color_normal, num_results))
    for package in json_data["results"]:
        package_name = package["Name"]
        print("{0}Name:{1} {2}".format(configuration.color_search_heading, configuration.color_normal, package_name))
        package_version = package["Version"]
        print("{0}Version:{1} {2}".format(configuration.color_search_heading, configuration.color_normal, package_version))
        package_maintainer = package["Maintainer"]
        print("{0}Maintainer:{1} {2}".format(configuration.color_search_heading, configuration.color_normal, package_maintainer))
        package_description = package["Description"]
        print("{0}Description:{1} {2}".format(configuration.color_search_heading, configuration.color_normal, package_description))
        nth_iteration += 1
        if num_results > 1 and not nth_iteration == num_results:
            print("\n")

def search(package_name):
    if configuration.search_type == "none" or configuration.search_type == None:
        rpc_url = "https://aur.archlinux.org/rpc/?v=5&type=search&arg={0}".format(package_name)
    else:
        rpc_url = "https://aur.archlinux.org/rpc/?v=5&type=search&by={0}&arg={1}".format(configuration.search_type, package_name)
    search_data = urllib.request.urlopen(rpc_url) #get json
    search_data = json.loads(search_data.read()) #decode json to python
    pretty_print_json(search_data) #pretty print json data 
