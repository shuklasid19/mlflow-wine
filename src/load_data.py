#read data from data source
#save it in the data/raw for further process


import pandas as pd
import argparse
import os
from get_data import read_params, get_data

def load_and_save(config_path):
    """were using function defined in get_data file
    read_params and get_data both take config_file loc 
    """
    config =  read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ","_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=',', index=False, header=new_cols)
    print(df.head())


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args  = args.parse_args()
    load_and_save(config_path=parsed_args.config)

