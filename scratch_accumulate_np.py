from datetime import datetime
from datetime import timedelta
import numpy as np


l_time_list = [['Person_1 Name', '07:01', '08:02'], ['Person_2 Name', '09:01', '10:02']]

np_rec_full = np.array(l_time_list)

np_rec_time = np.array(np_rec_full[:, 1:])

time_sum = []
list_array = []

for ctr, t in enumerate(np_rec_time):
    conv_to_time = [(datetime.strptime(str(x), '%M:%S')).time() for x in t]

    row_list = []
    t_accumulate_tdelta = timedelta(minutes=00, seconds=00)

    for date_time in conv_to_time:

        # convert to timedelta to do sum
        t_val_tdelta = timedelta(minutes=date_time.minute, seconds=date_time.second)
        t_accumulate_tdelta = t_accumulate_tdelta + t_val_tdelta

        # convert back to time
        t_val_time = (datetime.strptime(str(t_val_tdelta), '%H:%M:%S')).time()
        t_accumulate_time = (datetime.strptime(str(t_accumulate_tdelta), '%H:%M:%S')).time()

        # build datetime row including accumulated value
        row_list.append(t_val_time)
        if t_val_time != t_accumulate_time:
            row_list.append(t_accumulate_time)

    # build datetime array
    list_array.append(row_list)

# add datetime values to original rows
full_time_list = np.append(np_rec_full, list_array, axis=1)
print(full_time_list)


