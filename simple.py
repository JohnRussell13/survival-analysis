import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rawData = [2, 5, 7, 1, 3, 4, 6, 2, 4, 2, 3, 5, 1, 3, 6, 3, 2, 1, 2, 4]
sortedRawData = np.sort(rawData)

columns = ['Time', 'Start', 'Fail', 'Censored', 'At Risk', 'Surv Prob', 'Cum Surv']
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

    P_old = P
    currentCount = n - d - w
    row = [t, n, d, w, r, P, S]
    lifeTable.loc[len(lifeTable)] = row

print(lifeTable)

plt.plot(lifeTable['Time'], lifeTable['Cum Surv'])
plt.grid()
plt.title('Cumulative Survival Probability')
plt.xlabel('Time')
plt.ylabel('Probability')
plt.show()
