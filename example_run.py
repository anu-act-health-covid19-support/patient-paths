import numpy as np
from patientpaths import outcomes_for_moc

# for 4 cohorts, the mild presentations per day
di_mild = np.array([
[10, 10, 15, 15, 18, 21, 24, 32, 33, 30, 39, 36, 31, 26, 15, 11, 8, 4, 13, 14, 10, 16, 20, 20, 15, 24, 28, 26, 23, 19, 21, 14, 17, 5, 13, 12], 
[8, 20, 17, 16, 19, 20, 19, 22, 20, 30, 28, 22, 18, 11, 7, 5, 3, 2, 9, 12, 10, 17, 12, 21, 15, 22, 16, 22, 14, 12, 14, 10, 9, 8, 6, 4], 
[1, 10, 13, 10, 8, 5, 9, 11, 20, 40, 33, 21, 20, 20, 18, 14, 13, 11, 11, 13, 9, 17, 4, 5, 12, 14, 11, 26, 16, 10, 16, 11, 21, 17, 15, 6], 
[1, 3, 5, 9, 9, 11, 2, 5, 1, 2, 5, 7, 5, 8, 5, 7, 4, 5, 1, 9, 11, 11, 11, 10, 3, 10, 12, 5, 11, 8, 3, 13, 12, 7, 4, 7]
])
# for 4 cohorts, the sever presentations per day
di_sev = np.array([
[8, 0, 7, 6, 5, 2, 2, 4, 12, 4, 9, 1, 9, 4, 6, 3, 11, 1, 2, 12, 10, 6, 13, 4, 7, 3, 10, 10, 12, 11, 8, 12, 12, 10, 1, 6], 
[12, 8, 9, 15, 8, 8, 9, 10, 8, 11, 15, 9, 13, 17, 15, 10, 2, 10, 9, 13, 11, 14, 13, 12, 9, 6, 7, 8, 16, 9, 9, 5, 9, 12, 7, 3], 
[12, 10, 10, 7, 4, 7, 1, 12, 8, 1, 12, 12, 9, 5, 13, 3, 11, 4, 12, 14, 4, 9, 6, 14, 10, 9, 7, 12, 13, 6, 12, 9, 13, 11, 6, 3], 
[0, 9, 1, 2, 7, 4, 4, 8, 10, 8, 5, 10, 1, 13, 8, 4, 5, 6, 6, 14, 14, 2, 13, 4, 6, 6, 5, 1, 8, 8, 0, 10, 13, 3, 5, 11]
])

di_mild *= 10
di_sev *= 7

# cohorts 2 and 3 at risk
risk = np.array([0, 2, 2, 0])

cohorts = di_mild.shape[0]
days = di_mild.shape[1]
outcome = outcomes_for_moc("cohort", di_mild, di_sev, risk)

print("DEATHS PER COHORT")
print("\t".join([str(i) for i in range(1,cohorts+1)]))
print('-'*50)
for i in range(days):
	print("\t".join([str(a) for a in list(outcome['deaths'][i].round(decimals=2))]))
