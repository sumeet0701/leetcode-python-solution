from src.exception import CreditScoreException
from src.constant import *
import os
import sys
import numpy as np
import pandas as pd
import yaml
import dill

def write_yaml_file(file_path:str,data:dict=None):
    """
    Create yaml file 
    file_path: str
    data: dict
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path,"w") as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
    except Exception as e:
        raise CreditScoreException(e,sys)

# ----------------------------------------------------------------------------------------

def read_yaml_file(file_path:str)-> dict:
    """
    Read a yaml file and return the content as dictionary

    param:
    --------------------------------
    file_path(str) : file path for the yaml file
    """
    try:
        with open(file_path, "rb") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise CreditScoreException(e, sys) from e

#----------------------------------------------------------------

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise CreditScoreException(e, sys) from e
#----------------------------------------------------------------
    

def save_object(file_path:str, object):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok= True)
        with open(file_path, "wb") as f:
            dill.dump(object, f)
    except Exception as e:
        raise CreditScoreException(e, sys) from e
#----------------------------------------------------------------
    

def load_object(file_path:str):

    try:
        with open(file_path,"rb") as f:
            return dill.load(f)
    except Exception as e:
        raise CreditScoreException(e, sys) from e
#----------------------------------------------------------------



def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(schema_file_path)
        schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
        dataframe = pd.read_csv(file_path)
        error_message = ""
        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_message = f"{error_message} \nColumn: [{column}] is not in the schema."
        if len(error_message) > 0:
            raise Exception(error_message)
        return dataframe

    except Exception as e:
        raise CreditScoreException(e, sys) from e
#------------------------------------------------------------------------------


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj, allow_pickle=True)
    except Exception as e:
        raise CreditScoreException(e, sys) from e
#----------------------------------------------------------------



def save_data(file_path:str, data: pd.DataFrame):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        data.to_csv(file_path, index= None)
    except Exception as e:
        raise CreditScoreException(e, sys) from e
#----------------------------------------------------------------