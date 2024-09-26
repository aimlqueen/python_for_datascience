import statistics
lst = [2,5,6,9]
# mean
print(f"mean of the list {lst} is {statistics.mean(lst)}")
print(statistics.mean([1,2,3,4,5]))

#median
print(statistics.median([1,2,3,8,9]))
print(statistics.median([1,2,3,7,8,9]) )

#mode
print(statistics.mode([2,5,3,2,8,3,9,4,2,5,6]))

#Standard Deviation
print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))

#variance
print(statistics.variance([1, 2, 3, 4, 5]))


