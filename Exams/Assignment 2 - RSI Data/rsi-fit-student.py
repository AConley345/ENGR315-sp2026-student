import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path_to_datafile = "../../data/drop-jump/all_participant_data_rsi.csv"

#Below is the path to file for my device
#C:\\Users\\austi\\OneDrive\\Documents\\GitHub\\ENGR315-sp2026-student\\data\\drop-jump\\all_participant_data_rsi.csv"

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')   # question one section print

df = pd.read_csv(path_to_datafile)     # read the reference csv file
print(df.columns)                   # print the data columns

fp_rsi = df['force_plate_rsi']      # extract fp data from df
accel_rsi = df['accelerometer_rsi']         # extract accelerometer data from df

mu_fp = np.mean(fp_rsi)             # calculate mu for the fp
std_fp = np.std(fp_rsi)             # calculate std for the fp

mu_accel = np.mean(accel_rsi)       # calculate mu for the accel data
std_accel = np.std(accel_rsi)       # calculate std for the accel data

print('Force plate Data: mean =', mu_fp, 'std=', std_fp) # print mean and std for the fp
print('Accelerometer Data: mean =', mu_accel, 'std=', std_accel) # print the mean and std for the accelerometer

print('Accelerometer RSI (min/max): min =', min(accel_rsi), 'max = ', max(accel_rsi)) # finding max and min of accel to find x range
print('Force Plate RSI (min,max): min =', min(fp_rsi), 'max = ', max(fp_rsi))   # finding max and min of fb to find y range

x = np.linspace(start=0, stop=1.5, num=10000)   # create x-value parameters for normal distributions

fp_y = norm.pdf(x, mu_fp, std_fp)    # find normal distribution for fp
accel_y = norm.pdf(x, mu_accel, std_accel)    # find normal distribution for accel

plt.plot(x, accel_y, label='Acceleration Normal Fit') # plotting the norm for the accel
plt.plot(x, fp_y, label='Force Plate Normal Fit')  # plotting the norm for the fp


plt.title("RSI Normal Distributions") # titling the plot
plt.xlabel("RSI")   # x-axis label on the plot
plt.ylabel("Probability")   # y-axis label on the plot

plt.legend() # write legend for the plots were labeled previously
plt.show()  # display the plot when code is ran
plt.savefig("my_plot.png") # save the generated graph


"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')   # question two section print

alpha = 0.05    # define alpha

bins = np.linspace(0, 2, 9) # bin edges between [0,2) as constrained

bins = np.r_[-np.inf, bins, np.inf] # add -inf and +inf to bins

"""
Acceleration
"""

observed_counts_accel, observed_edges_accel = np.histogram(accel_rsi, bins=bins, density=False) # place observations in bins for accel data

expected_prob_accel = np.diff(norm.cdf(bins, loc=mu_accel, scale=std_accel))    # calculate expected probability of accel data falling into the created bin
expected_counts_accel = expected_prob_accel * len(accel_rsi)    # expected frequency for each bin for accel data

(chi_accel, p_accel) = chisquare(f_obs=observed_counts_accel, f_exp=expected_counts_accel, ddof=2) # calcualte chi2 stat and p-value for accel data


print('Accelerometer Data:') # printed acceleration data
print('Chi2 accelerometer: ', chi_accel, ', p-value accelerometer: ', p_accel) # print chi2 stat and p-value for accel data
if p_accel < alpha: # if statement to print if it is a good fit or not
    print('Accelerometer normal distribution is not a good fit.')
else:
    print('Accelerometer normal distribution is a good fit.')


"""
Force Plate
"""
observed_counts_fp, observed_edges_fp = np.histogram(fp_rsi, bins=bins, density=False)  # place observations in bins for fp data

expected_prob_fp = np.diff(norm.cdf(bins, loc=mu_fp, scale=std_fp)) # calculate expected probability of fp data falling into the created bin
expected_counts_fp = expected_prob_fp * len(fp_rsi) # expected frequency for each bin for fp data

(chi_fp, p_fp) = chisquare(f_obs=observed_counts_fp, f_exp=expected_counts_fp, ddof=2)  # calcualte of chi2 stat and p-value for fp data


print('Force plate Data:')  # printed fp data
print('Chi2 stat force plate: ', chi_fp, ', p-value force plate: ', p_fp) # print chi2 stat and p-value for fp data
if p_fp < alpha:    # if statement to print if it is a good fit or not
    print('Force Plate normal distribution is not a good fit.')
else:
    print('Force Plate normal distribution is a good fit.')


"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')   # question three section print


(t_stat, p_val) = ttest_ind(fp_rsi, accel_rsi, alternative='two-sided') # ind t-test to compare fp and accel data

print('t-stat = ', t_stat)  # print of the t-stat value
print('p-val = ', p_val)    # print of the p-value

if p_val < alpha:   # determine if there is a difference between fp mean and accel mean
    print('The p-value is less than 0.05 therefore the means are not equal.')
else:
    print('The p-value is greater than 0.05 therfore the means are equal.')


"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE