import numpy as np  # funkcje numpy median, mean, std, min, max
import statistics as st  # statistics median_high(), median_law(), pstdev(), stdev(), pvariance(), variance(), mode()
import scipy.stats as sc
import pandas as pd
import matplotlib.pyplot as plt

dane = np.loadtxt("MDR_RR_TB_burden_estimates_2020-10-29.csv", delimiter=',', skiprows=1, usecols=12)
# print(dane)

print(np.max(dane))
print(dane.max())
print(np.median(dane))

dane1 = np.loadtxt("Wzrost.csv", delimiter=',', skiprows=0)
# print(dane1)

print("odchylenie standardowe:", st.stdev(dane1))
print("odchylenie standardowe 2", st.pstdev(dane1))
print("median high:", st.median_high(dane1))
print("median low:", st.median_low(dane1))
print("pstdev:", st.pstdev(dane1))
print("stdev:", st.stdev(dane1))
print("pvariance:", st.pvariance(dane1))
print("variance:", st.variance(dane1))
print("mode:", st.mode(dane1))

print(sc.ttest_1samp(dane, 0))

df = pd.read_csv("brain_size.csv", delimiter=";", skiprows=0)
# print(df)

print(np.mean(df['VIQ']))
print(df['Gender'].value_counts())

X = np.arange(0, len(df.index))
plt.plot(X, df['VIQ'])
plt.plot(X, df['PIQ'])
plt.plot(X, df['FSIQ'])
plt.show()

fem = df.loc[df['Gender'] == 'Female']
x_row = np.arange(0, len(fem.index))
plt.plot(x_row, fem['VIQ'])
plt.plot(x_row, fem['PIQ'])
plt.plot(x_row, fem['FSIQ'])
plt.show()
