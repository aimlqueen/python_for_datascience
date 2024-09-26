# Import statistics Library
import statistics

# Calculate harmonic mean
print(statistics.harmonic_mean([40, 60, 80]))
print(statistics.harmonic_mean([10, 30, 50, 70, 90]))

# Calculate the median of grouped continuous data
print(statistics.median_grouped([1, 2, 3, 4]))
print(statistics.median_grouped([1, 2, 3, 4, 5]))
print(statistics.median_grouped([1, 2, 3, 4], 2))
print(statistics.median_grouped([1, 2, 3, 4], 3))
print(statistics.median_grouped([1, 2, 3, 4], 5))


# Calculate the high middle values
print(statistics.median_high([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median_high([1, 3, 5, 7, 9, 11]))
print(statistics.median_high([-11, 5.5, -3.4, 7.1, -9, 22]))


# Calculate the low middle values
print(statistics.median_low([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median_low([1, 3, 5, 7, 9, 11]))
print(statistics.median_low([-11, 5.5, -3.4, 7.1, -9, 22]))

# Calculate the standard deviation from an entire population
print(statistics.pstdev([1, 3, 5, 7, 9, 11]))
print(statistics.pstdev([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.pstdev([-11, 5.5, -3.4, 7.1]))
print(statistics.pstdev([1, 30, 50, 100]))