#important
# there is another suggestion to better use timeit library
# https://docs.python.org/3/library/timeit.html
# TODO - check it out when needed.


import time

start_time = time.time()
# Code to check follows
a, b = 1,2
c = a+ b
# Code to check ends
end_time = time.time()
time_taken_in_micro = (end_time- start_time)*(10**6)

print(" Time taken in micro_seconds: {0} ms").format(time_taken_in_micro)