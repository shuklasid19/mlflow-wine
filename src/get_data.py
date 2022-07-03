#read parameters file params
#process 
#return dataframe

import pandas  as pd
import numpy as np
import os
import yaml
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config  = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    """config file contains all the parameters dictionary 
    it return all key,value pairs that are in params.yaml file
       #dataset 
       #print(config) all parameters key,val
    """

    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    return df
 




if __name__=="__main__":
    """were basically sending the config file params.yaml from here
    """
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args  = args.parse_args()
    get_data(config_path=parsed_args.config)








