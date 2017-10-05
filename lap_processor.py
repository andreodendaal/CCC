import csv
import numpy as np
import pandas as pd
from datetime import datetime
import time


class Lap_processor:

    def __init__(self, filename):
        # str2date = lambda x: datetime.strptime(x.decode("utf-8"), '%H:%M:%S')

        race = np.genfromtxt(filename, delimiter=",", dtype=str)
        #print(race)
        racer_laps = race[1: , 7:]
        #print(racer_laps)
        laps = racer_laps.T
        #print(laps[0])

        print(laps[0][0])
        lap_value = laps[0][0]
        lap_value_time = (datetime.strptime(str(lap_value), '%M:%S')).time()
        print(lap_value_time)

        laps_timed = [(datetime.strptime(str(x), '%M:%S')).time() for x in laps[0]]
        print(laps_timed[0])
        print(laps_timed)
        laps_timed.sort()
        print(laps_timed)





         #lap_times = racer_laps.transpose()

        #print(lap_times[0])



if __name__ == '__main__':

    my_lap = Lap_processor("2017 CCC Lap Times - Hopkins Park.csv")