import configparser
import os
from os.path import abspath

config = configparser.ConfigParser()
config.read(abspath(os.environ["CONFIG"]))

