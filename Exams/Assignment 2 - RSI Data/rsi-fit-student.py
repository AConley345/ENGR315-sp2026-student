import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path_to_datafile = "C:\\Users\\austi\\OneDrive\\Documents\\GitHub\\ENGR315-sp2026-student\\data\\drop-jump\\all_participant_data_rsi.csv"

### YOUR CODE HERE

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

df = pd.read_csv(path_to_datafile)     # read the csv file that is being reference
print(df.columns)                   # print the data to see what is included

fp_rsi = df['force_plate_rsi']      # making variable for the force plate column from the data
accel_rsi = df['accelerometer_rsi']         # making varaible for the acceleromter column from the data

mu_fp = np.mean(fp_rsi)             # finding mu for the fp
std_fp = np.std(fp_rsi)             # finding std for the fp

mu_accel = np.mean(accel_rsi)       # finding mu for the accel data
std_accel = np.std(accel_rsi)       # finding std for the accel data

print('Force plate Data - mean =', mu_fp, 'std=', std_fp) # print mean and std for the fp
print('Acceleromter Data - mean =', mu_accel, 'std=', std_fp) # print the mean and std for the acceleromter

print('Accel min =', min(accel_rsi), 'max = ', max(accel_rsi)) # finding max and min of fp to find x range
print('Forceplate min =', min(fp_rsi), 'max = ', max(fp_rsi))   # finding max and min of fb to find y range

x = np.linspace(start=0, stop=1.5, num=10000)   # x range from 0-1.5 with 10000 points

fp_y = norm.pdf(x, mu_fp, std_accel)    # find norm for fp
accel_y = norm.pdf(x, mu_fp, std_fp)    # find norm for accel

plt.plot(x, accel_y, label='Forceplate Normal Fit') # plotting the norm for the fp
plt.plot(x, fp_y, label='Acceleration Normal Fit')  # plotting the norm for the accel


plt.title("RSI Normal Distributions") # titling the plot
plt.xlabel("RSI")   # x-axis label on the plot
plt.ylabel("Probability")   # y-axis label on the plot

plt.legend() # write legend for the plots were labeled previosely
plt.show()  # display the plot when code is ran
### YOUR CODE HERE


"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

alpha = 0.05

bins = np.linspace(-2, 2, 9)

bins = np.r_[-np.inf, bins, np.inf]
"""
Acceleration
"""

observed_counts_accel, observed_edges_accel = np.histogram(accel_rsi, bins=bins, density=False)

expected_prob_accel = np.diff(norm.cdf(bins, loc=mu_accel, scale=std_accel))
expected_counts_accel = expected_prob_accel * len(accel_rsi)

(chi_accel, p_accel) = chisquare(f_obs=observed_counts_accel, f_exp=expected_counts_accel, ddof=2)


print('Acceleration Data:')
print('Chi2 accelerometer: ', chi_accel, 'p-value accelerometer: ', p_accel)
if p_accel < alpha:
    print('Reject null hypothesis. Counts are not equal.')
else:
    print('Accept null hypothesis. Counts are equal')

### YOUR CODE HERE

"""
Force Plate
"""
observed_counts_fp, observed_edges_fp = np.histogram(fp_rsi, bins=bins, density=False)

expected_prob_fp = np.diff(norm.cdf(bins, loc=mu_fp, scale=std_fp))
expected_counts_fp = expected_prob_fp * len(fp_rsi)

(chi_fp, p_fp) = chisquare(f_obs=observed_counts_fp, f_exp=expected_counts_fp, ddof=2)


print('Force plate Data:')
print('Chi2 stat force plate: ', chi_fp, 'p-value force plate: ', p_fp)
if p_fp < alpha:
    print('Reject null hypothesis. Counts are not equal.')
else:
    print('Accept null hypothesis. Counts are equal')

### YOUR CODE HERE

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE

"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE