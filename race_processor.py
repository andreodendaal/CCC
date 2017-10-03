import pandas as pd
import numpy as np

def file_reader():
    df = pd.read_csv('2017 CCC Lap Times - Hopkins Park.csv')
    print(df.columns.values)
    #print([df])
    print(df.loc[df['Last'] == 'ODENDAAL'])
    num_laps = number_of_laps(df)


def lap_processor():
    pass

def lap_analytics():

def number_of_laps(df):
    '''
    
    :return: 
    '''
    laps = num for num in df.columns.values if num like 'lap%'
return num_of_laps


if __name__ == '__main__':
    file_reader()