import csv
import numpy as np
import pandas as pd
from datetime import datetime
import time


class Lap_processor:

    def __init__(self, filename):
        # str2date = lambda x: datetime.strptime(x.decode("utf-8"), '%H:%M:%S')

        race = np.genfromtxt(filename, delimiter=",", dtype=str)
        print("printing race file...")
        print(race)
        racer_laps = race[1: , 7:]

        print("printing laps file by racer")
        print(racer_laps)

        laps = racer_laps.transpose()

        print("lap formatting tests")
        print(laps[0][0])
        lap_value = laps[0][0]
        lap_value_time = (datetime.strptime(str(lap_value), '%M:%S')).time()
        print(lap_value_time)
        # create grid of times per laps

        laps_timed = [(datetime.strptime(str(x), '%M:%S')).time() for x in laps[0] if x != '']
        print(laps_timed[0])
        print("\n Lap times grid formatted to time object....")
        print(laps_timed)

        # sort laps for reference
        print("\n Lap times grid formatted sorted...")
        laps_timed.sort()
        print(laps_timed)

        #lap_times = racer_laps.transpose()

        for i in racer_laps:
            for t in i:
                if t != '':
                    #print(t)
                    t_time = (datetime.strptime(str(t), '%M:%S')).time()
                    print(t_time in laps_timed)



if __name__ == '__main__':

    my_lap = Lap_processor("test.csv")