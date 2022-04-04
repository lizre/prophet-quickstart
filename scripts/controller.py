#!/usr/bin/env python 3

import argparse
from pathlib import Path
from setuptools import find_packages, setup
import os
import timeit
import yaml
import requests
#from schema import Schema, SchemaError
from pprint import pformat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error
from typing import Any, Dict, List, Tuple
#from fbprophet import Prophet
#import snakemd

import functions

with open(Path("requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

functions.get_data(limit="10")