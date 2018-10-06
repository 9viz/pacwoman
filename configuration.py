import yaml
import os

# write config file path name in $HOME/.cache/pacwoman/configpath
def writeConfigDir(config_path):
    path = os.path.join(os.getenv("HOME"), ".cache", "pacwoman")

    if not os.path.exists(path):
        os.mkdir(path)

    with open(os.path.join(path, "config_path"), "w+") as file_config_path:
        file_config_path.write(config_path)

# read config file directory
def getConfigDir():
    global config_path
    path = os.path.join(os.getenv("HOME"), ".cache", "pacwoman", "config_path")

    with open(path, "r") as file_config_path:
        config_path = file_config_path.read()

    config_path.strip("\n")

# decode yaml data
def readConfig(file_name):
    global config 

    with open(file_name.strip("\n"), "r") as config_file:
        config = yaml.load(config_file) 


## TODO: below
if not os.path.isfile("{0}/.cache/pacwoman/config_path".format(os.getenv("HOME"))):
    readConfig("{0}/res/config.yaml".format(os.path.realpath(__file__).strip("configuration.py")))
else:
    getConfigDir()
    readConfig(config_path)

# set all variables
insults = config["insults"]
colored_output = config["colored_output"]
color_normal = bytes(config["color_normal"], "utf-8").decode("unicode_escape")
color_error = bytes(config["color_error"], "utf-8").decode("unicode_escape")
color_successful = bytes(config["color_successful"], "utf-8").decode("unicode_escape")
color_progress = bytes(config["color_progress"], "utf-8").decode("unicode_escape")
color_search_heading = bytes(config["color_search_heading"], "utf-8").decode("unicode_escape")
cd_to_package = config["cd_to_package"]
root_execute = config["root_execute"]
search_type = config["search_type"]
