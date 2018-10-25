import yaml
import os

# write config file path name in $HOME/.cache/pacwoman/configpath
def write_config_dir(config_path):
    path = os.path.join(os.getenv("HOME"), ".cache", "pacwoman")

    if not os.path.exists(path):
        os.mkdir(path)

    with open(os.path.join(path, "config_path"), "w+") as file_config_path:
        file_config_path.write(config_path)

# read config file directory
def get_config_dir():
    global config_path
    path = os.path.join(os.getenv("HOME"), ".cache", "pacwoman", "config_path")

    with open(path, "r") as file_config_path:
        config_path = file_config_path.read()

    config_path.strip("\n")

# decode yaml data
def read_config(file_name):
    global config 

    with open(file_name.strip("\n"), "r") as config_file:
        config = yaml.load(config_file) 

get_escape_seq = lambda str_seq: bytes(str_seq, "utf-8").decode("unicode_escape")

file_config_path = os.path.join(os.getenv("HOME"), ".cache",\
        "pacwoman", "config_path")
default_config_path = os.path.join(os.path.abspath(__file__)\
        .strip("configuration.py"), "res", "config.yaml")

if os.path.isfile(file_config_path): 
    get_config_dir()
    read_config(config_path)
else:
    read_config(default_config_path)

# set all variables
insults = config.get("insults", False)
colored_output = config.get("colored_output")
color_normal = get_escape_seq(config.get("color_normal", "")) 
color_error = get_escape_seq(config.get("color_error", ""))
color_successful = get_escape_seq(config.get("color_successful", ""))
color_progress = get_escape_seq(config.get("color_progress", ""))
color_search_heading = get_escape_seq(config.get("color_search_heading", ""))
cd_to_package = config.get("cd_to_package")
root_execute = config.get("root_execute")
search_type = config.get("search_type", None)
