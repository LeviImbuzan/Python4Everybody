import numpy as np
from scipy import stats

numbers = np.array([5,7,10,10,13,15])
numbers.sort()

mean = np.average(numbers)
median = np.median(numbers)
mode = stats.mode(numbers)

print("Mean is = " + str(mean) + ", " "Median is = " + str(median) + ", " , "Mode is = " + str(mode))
