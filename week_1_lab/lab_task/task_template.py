import numpy as np

# Hint: To visualize the data, you can import matplotlib.pyplot as plt

# Step 1: Load the CSV file using numpy
# HINT: Use np.loadtxt, specifying the path to your CSV, delimiter, and skiprows to ignore the header

data = np.loadtxt('<PATH_TO_CSV>', delimiter=',', skiprows=1)

# Extract the days and temperatures from the loaded data
days = data[:, 0]
temperatures = data[:, 1]

# Step 2: Calculate the mean and standard deviation of the temperatures
# HINT: Use np.mean and np.std functions

mean_temperature = np.mean(temperatures)
std_temperature = np.std(temperatures)

# Step 3: Identify the hottest and coldest days
# HINT: Use the mean and standard deviation to calculate thresholds for hot and cold days.
# Hot days could be defined as days with temperatures more than 2 standard deviations above the mean
# Cold days could be defined as days with temperatures more than 2 standard deviations below the mean

hot_threshold = mean_temperature + 2 * std_temperature
cold_threshold = mean_temperature - 2 * std_temperature

# Find the days that are hotter than the hot_threshold and colder than the cold_threshold
# HINT: Use boolean indexing with days and temperatures arrays

hot_days = days[temperatures > hot_threshold]
cold_days = days[temperatures < cold_threshold]

# Step 4 (Optional): Visualize the data using matplotlib
# Plot the temperatures across days and mark the hot and cold days using different colors or markers
# HINT: Use plt.plot for the temperatures, plt.scatter for marking hot and cold days

# YOUR CODE HERE for visualization

# Step 5: Write a summary of your findings
# Create a string variable `summary` that includes the mean temperature, standard deviation,
# and lists of hot and cold days.

summary = f"""
Mean Temperature: {mean_temperature:.2f}C
Standard Deviation: {std_temperature:.2f}C
Hottest Days: {hot_days}
Coldest Days: {cold_days}
"""

# Print the summary
print(summary)