import pandas as pd
import numpy as np
import scipy.stats as scs
import statistics as st
import matplotlib.pyplot as plt

d = {'wartosc': [1, 2, 3, 4, 5, 6], 'prawdopodobienstwo': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]}
df = pd.DataFrame(data=d)

# Exercise 1

print('max', np.max(df['wartosc']))
print('min', np.min(df['wartosc']))
print("std", np.std(df['wartosc']))
print('mean', np.mean(df['wartosc']))

# Exercise 2
ber = scs.bernoulli.rvs(0.3, size=100)
bim = scs.binom.rvs(1, 0.3, size=100)
poi = scs.poisson.rvs(0.3, size=100)

# print('bernoulli', ber)
# print('binom', bim)
# print('poisson', poi)

# Exercise 3

# print('Bernoulli mean', np.mean(ber))
# print('Binom mean', np.mean(bim))
# print('Poisson mean', np.mean(poi))
#
# print('\nBernoulli variance', st.variance(ber))
# print('Binom variance', st.variance(bim))
# print('Poisson variance', st.variance(poi))
#
# print('\nBernoulli kurtosis', scs.kurtosis(ber))
# print('Binom kurtosis', scs.kurtosis(bim))
# print('Poisson kurtosis', scs.kurtosis(poi))
#
# print('\nBernoulli skewnes', scs.skew(ber))
# print('Binom skewnes', scs.skew(bim))
# print('Poisson skewnes', scs.skew(poi))


# Exercise 4

X = np.arange(0, 100)
# plt.plot(X, ber)
# plt.plot(X, bim)
# plt.plot(X, poi)
# plt.show()

# Exerise 5

bim1 = scs.binom.pmf(20, 20, 0.4)
# print(np.sum(bim1))
# print(bim1)

# Exercise 6

nor = scs.norm.rvs(0, 2, 100)
# print('max', np.max(nor))
# print('min', np.min(nor))
# print("std", np.std(nor))
# print('mean', np.mean(nor))

# Exercise 7

nor1 = scs.norm.rvs(1, 2, 100)
den = scs.norm.pdf(nor1, loc=-1, scale=0.5)
plt.plot(X, nor1)
plt.plot(X, den)
plt.show()
# print(den)
