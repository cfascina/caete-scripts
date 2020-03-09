import math
import pandas as pd


def photosynthesis_penalty(umol_penalty, leaf_critical_age, leaf_middle_age):
    return min(1, math.exp(umol_penalty * (leaf_critical_age - leaf_middle_age)))


# Photosynthesis penalty values for each coorte
# Original: 12 / 30 / 20  - (umol* CO2) /  m² *  s^1)
umol_penalties = [-0.4, 1, 0.6]

# The variable "age_crit" will be derived from carbon residence time (CAETÊ variable trait)
residence_time = 6
critical_age = residence_time / 3 * 2

# Calculates age limits for each coorte
age_limits = [critical_age / 2, critical_age, critical_age / 2 * 3]

# Calculates the middle age for each coorte##
middle_ages = []
for index, value in enumerate(age_limits):
    if index == 0:
        middle_ages.append((0 + age_limits[index]) / 2)
    else:
        middle_ages.append((age_limits[index] + age_limits[index - 1]) / 2)

# Counting time at annual scale
results = []
for age in age_limits:
    if age <= age_limits[0]:
        results.append(photosynthesis_penalty(umol_penalties[0], critical_age, middle_ages[0]))
    elif age_limits[0] < age <= age_limits[1]:
        results.append(photosynthesis_penalty(umol_penalties[1], critical_age, middle_ages[1]))
    elif age_limits[1] < age <= age_limits[2]:
        results.append(photosynthesis_penalty(umol_penalties[2], critical_age, middle_ages[2]))
    else:
        results.append("Leaf age outside coorte limits.")

# Organizing and plotting the data
data = {
    "umol_penalty": pd.Series(umol_penalties),
    "age_limit": pd.Series(age_limits),
    "middle_age": pd.Series(middle_ages),
    "result": pd.Series(results)}

data_frame = pd.DataFrame(data)
print(data_frame)
