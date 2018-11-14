# -*- coding: utf-8 -*-
"""
raster_tools.py # Introduces raster functions. Needs to be in the same directory than the calling function

Useful functions related to raster processing

Created on Wed Nov 14 10:26:00 2018

@author: nkulha
"""

import numpy as np
import json

def normalize(array):
    """Normalizes numpy arrays into scale 0.0 - 1.0"""
    """Used in raster processing, but can eat any kind of data"""
    array_min, array_max = array.min(), array.max()
    return ((array - array_min) / (array_max - array_min))


def get_features(gdf):
    """Converts GeoDataFrame into a format how rasterio
    mask function wants to have the 
    geometric features.
    """
    features = [json.loads(gdf.to_json())['features'][0]['geometry']]
    return features