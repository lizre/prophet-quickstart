#!/usr/bin/eng python 3

import pandas as pd

def pandas_startup():
    options = {
        'display': {
            'max_columns': None,
            'expand_frame_repr': False,
            'max_rows': 20,
            'max_seq_items': 50,
            'precision': 4,
            'float_format': lambda x: '%.3f' % x
        }
    }


    for category, option in options.items():
        for op, value in option.items():
            pd.set_option(f'{category}.{op}', value)