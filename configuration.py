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

getEscapeSeq = lambda str_seq: bytes(str_seq, "utf-8").decode("unicode_escape")

file_config_path = os.path.join(os.getenv("HOME"), ".cache",\
        "pacwoman", "config_path")
default_config_path = os.path.join(os.path.abspath(__file__)\
        .strip("configuration.py"), "res", "config.yaml")

if os.path.isfile(file_config_path): 
    getConfigDir()
    readConfig(config_path)
else:
    readConfig(default_config_path)

# set all variables
insults = config.get("insults", False)
colored_output = config.get("colored_output")
color_normal = getEscapeSeq(config.get("color_normal", "")) 
color_error = getEscapeSeq(config.get("color_error", ""))
color_successful = getEscapeSeq(config.get("color_successful", ""))
color_progress = getEscapeSeq(config.get("color_progress", ""))
color_search_heading = getEscapeSeq(config.get("color_search_heading", ""))
cd_to_package = config.get("cd_to_package")
root_execute = config.get("root_execute")
search_type = config.get("search_type", None)
