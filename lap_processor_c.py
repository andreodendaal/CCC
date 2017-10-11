import pandas as pd
import numpy as np
from datetime import datetime

class LapProcessor:

    def __init__(self, filename):

        self.race = np.genfromtxt(filename, delimiter=",", dtype=str)

        # print(race)
        # Build times per lap grid
        self.race_laps = self.race[1:, 7:]
        print("racer Laps grid:", self.race_laps)
        self.laps_grid = self.race_laps.transpose()
        print("racer Laps grid transposed: ", self.laps_grid)

        # Format to date time so the laps can be sorted
        self.laps_grid_timeformat = []
        for lap in self.laps_grid:
            if lap[0] != '':
                self.laps_grid_timeformat.append([(datetime.strptime(str(x), '%M:%S')).time() for x in lap])

        for rec in self.laps_grid_timeformat:
            #print("\n")
            #print(rec)
            rec.sort()
            #print(rec)
            print(type(rec))

        #self.race_analytical = np.array(self.race)
        self.race_analytical = pd.DataFrame.from_records(self.race[1:], columns=self.race[0])
        #print(self.race_analytical)

    def process_laptime_position(self):

        header = 'lap 1 position'

        self.race_analytical[header] = np.where(self.race_analytical['Lap 1'] != '', (datetime.strptime(str('Lap 1'), '%M:%S')).time())

        # process the file headers create a lap position column for each lap raced
        print(self.race_analytical)
        print(len(self.race_analytical))


        # process each rider

        # process each lap

        # get the relative lap position

        # update the grid
        #evaluate the lap position, update the lap position field
        lap_value = self.laps_grid[0][0]
        lap_value_time = (datetime.strptime(str(lap_value), '%M:%S')).time()
        #print(lap_value_time)

        # test time lookup
        #print(lap_value_time in self.laps_grid_timeformat[0])
        position = (self.laps_grid_timeformat[0].index(lap_value_time)) + 1
        #print("position:", position)






if __name__ == '__main__':

    race = LapProcessor("2017 CCC Lap Times - Hopkins Park.csv")
    LapProcessor.process_laptime_position(race)
