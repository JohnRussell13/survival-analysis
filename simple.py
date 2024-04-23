import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rawData = [2, 5, 7, 1, 3, 4, 6, 2, 4, 2, 3, 5, 1, 3, 6, 3, 2, 1, 2, 4]
sortedRawData = np.sort(rawData)

columns = ['Time', 'Start', 'Fail', 'Censored', 'At Risk', 'Kaplan-Meier', 'Flemington-Harrington']
lifeTable = pd.DataFrame(columns=columns)

totalCount = np.size(sortedRawData)
maxTime = np.max(sortedRawData)

currentCount = totalCount
P_old = 1
for i in range(0, maxTime+1):
    t = i
    n = currentCount
    d = np.sum(sortedRawData == i)
    w = 0
    r = n - w
    if r == 0:
        break
    P = (r - d)/r
    S = P * P_old
    H = d/r

    P_old = P
    currentCount = n - d - w
    row = [t, n, d, w, r, S, H]
    lifeTable.loc[len(lifeTable)] = row

print(lifeTable)

time = range(0, maxTime+1)
kmSurvival = lifeTable['Kaplan-Meier'].values
kmHazard = -np.log(kmSurvival)

fhHazard = lifeTable['Flemington-Harrington'].values
fhSurvival = np.exp(-fhHazard)

plt.plot(time, kmSurvival, label='Kaplan-Meier')
# plt.plot(time, fhSurvival, label='Flemington-Herrington')
plt.grid()
plt.title('Survival Function')
plt.xlabel('Time')
plt.ylabel('Probability')
plt.legend()
plt.show()
