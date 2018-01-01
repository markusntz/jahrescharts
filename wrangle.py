# -*- coding: utf-8 -*-
"""
cleaning up the different parts
"""

import os
import glob
import pandas as pd

# load data
path = 'data/'                   
all_files = glob.glob(os.path.join(path, "*.csv"))
df = (pd.read_csv(f) for f in all_files)
tracks = pd.concat(df, ignore_index=True)

# get rid of sloppiness before
del tracks['Unnamed: 0']

# check for duplicates
tracks.shape
tracks.drop_duplicates()

# reorder
tracks.head(n=10)
tracks.tail(n=10)
tracks_sorted = tracks.sort_values(by=['played'])

# get artist + song
query = tracks_sorted['artist'] + ', ' + tracks_sorted['song']

# ask spotify for track id
# import requests
# ...