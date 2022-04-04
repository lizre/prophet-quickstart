import os
import argparse
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

def get_data(limit: str):
    """Get and clean data for use in forecasts. 

    Returns:
        pd.DataFrame
    """
    start = timeit.default_timer()
    data_path = os.path.join("data")
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    request_string = ("https://data.sfgov.org/resource/wg3w-h783.json?$limit="+limit+"&$offset=0&$order=:id")
    request_string
    r = requests.get(request_string)
    print("Requesting", limit, "rows from API...")
    assert(r.ok)
    print("API request status:", r)
    df = pd.read_json(r.text)
    df.to_csv(os.path.join(
                        "data",
                        'data.csv'), index=False)
    stop = timeit.default_timer()
    print("Got the data and put it in",
          data_path,
          ". It took",
          round(stop - start,0),
          "seconds.")
    return df
