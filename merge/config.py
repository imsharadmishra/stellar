import configparser
class Config:
    def __init__(self,conf_path):
        self.configparser = configparser.ConfigParser()
        self.conf_path = conf_path
        self.configparser.read(self.conf_path)
        
    def get_config_parser(self):
        return self.configparser

    def print_config_section(self,config,section):
        for key in config[section]:
            print(f"{key}->{config[section][key]}")