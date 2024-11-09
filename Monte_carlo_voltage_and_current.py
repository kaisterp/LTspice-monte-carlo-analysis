import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics

# --------------------------------------------------------------------------------------------
# A few things to note:
# 
# You have to enter the number of step of your monte carlo simulation below
# 
# Your spacing has to be the same in the CSV file (2 initial text rows, 4 identical data rows, one text row. repeated.)
# 
# You have to have 2 data columns (voltage and current in this case) SEE CSV FILES USED FOR THIS SCRIPT
# 
# You have to adjust the arrows spacing on the figures.
# 
# The rest is automated.
# --------------------------------------------------------------------------------------------



#get data from LTSpice txt: (csv at the moment)
file=np.genfromtxt("NMOS_BiasMC.csv",delimiter=",")
file = file[2:,1:]

#Choose number of rows (number of steps in Monte Carlo Simulation):
rows = 1000

# Extract wanted selected data(5 rows between each step in excel): (TODO: change this to import from TXT in future)
data = file[:rows,:]
i = 0
while i < rows:
    data[i,0] = file[5*i,0]
    data[i,1] = file[5*i,1]
    i = i + 1
# print(data)


#split voltage and current data:
voltage = data[:,0]
current = data[:,1]
# print(voltage)


#Find and print voltage stats:
mean = statistics.mean(voltage)
median = statistics.median(voltage)
stdev = statistics.stdev(voltage)
sigma3 = 3*stdev
print('VOLTAGE:')
print('mean:')
print(mean)
print('median:')
print(median)
print('stdev:')
print(stdev)
print('sigma3:')
print(sigma3)


# Select line parameters:
sigma_height = 2.5
sigma3_height = 2.7
text_line_spacing = 0.02
# Creating a customized histogram with a density plot
sns.histplot(voltage, bins=50, stat="density")                                                                      #Plot histogram
sns.kdeplot(voltage, color="orange")                                                                                #plots density line (kde line)

plt.axvline(x = mean+stdev, color = 'black', label = 'stdev - upper', ymax = 0.90, ls='--', lw=0.8)                 #Sigma upper line
plt.axvline(x = mean-stdev, color = 'black', label = 'stdev - lower', ymax = 0.90, ls='--', lw=0.8)                 #Sigma lower line
plt.annotate('', xy=((mean+stdev),sigma_height), xytext=(mean-stdev,sigma_height), arrowprops={'arrowstyle': '<->'}, va='center')     #Sigma arrow
plt.text(mean, sigma_height+text_line_spacing, 'σ')                                                                              #Sigma text

plt.axvline(x = mean+sigma3, color = 'black', label = '3sigma - upper', ymax = 0.95, ls='--', lw=0.8)                 #3Sigma upper line
plt.axvline(x = mean-sigma3, color = 'black', label = '3sigma - lower', ymax = 0.95, ls='--', lw=0.8)                 #3Sigma lower line
plt.annotate('', xy=((mean+sigma3),sigma3_height), xytext=(mean-sigma3,sigma3_height), arrowprops={'arrowstyle': '<->'}, va='center')     #3Sigma arrow
plt.text(mean, sigma3_height+text_line_spacing, '3σ')                                                                              #3Sigma text

plt.xlabel('Voltage (V)')
plt.ylabel('Relative Frequency')
plt.title('Monte Carlo Output Voltage Distribution Histogram')
plt.show()



# Uncomment to convert amps to mili amps -------------------
i = 0
while i < rows:
    current[i] = current[i]*1000
    i = i + 1
# ----------------------------------------------------------


# Find and print current stats:
mean = statistics.mean(current)
median = statistics.median(current)
stdev = statistics.stdev(current)
sigma3 = 3*stdev
print('CURRENT:')
print('mean:')
print(mean)
print('median:')
print(median)
print('stdev:')
print(stdev)
print('sigma3:')
print(sigma3)


# Select line parameters:
sigma_height = 7
sigma3_height = 7.5
text_line_spacing = 0.05
# Creating a customized histogram with a density plot
sns.histplot(current, bins=50, stat="density")                                                                      #Plot histogram
sns.kdeplot(current, color="orange")                                                                                #plots density line (kde line)

plt.axvline(x = mean+stdev, color = 'black', label = 'stdev - upper', ymax = 0.90, ls='--', lw=0.8)                 #Sigma upper line
plt.axvline(x = mean-stdev, color = 'black', label = 'stdev - lower', ymax = 0.90, ls='--', lw=0.8)                 #Sigma lower line
plt.annotate('', xy=((mean+stdev),sigma_height), xytext=(mean-stdev,sigma_height), arrowprops={'arrowstyle': '<->'}, va='center')     #Sigma arrow
plt.text(mean, sigma_height+text_line_spacing, 'σ')                                                                              #Sigma text

plt.axvline(x = mean+sigma3, color = 'black', label = '3sigma - upper', ymax = 0.95, ls='--', lw=0.8)                 #3Sigma upper line
plt.axvline(x = mean-sigma3, color = 'black', label = '3sigma - lower', ymax = 0.95, ls='--', lw=0.8)                 #3Sigma lower line
plt.annotate('', xy=((mean+sigma3),sigma3_height), xytext=(mean-sigma3,sigma3_height), arrowprops={'arrowstyle': '<->'}, va='center')     #3Sigma arrow
plt.text(mean, sigma3_height+text_line_spacing, '3σ')                                                                              #3Sigma text

plt.xlabel('Current (mA)')
plt.ylabel('Relative Frequency')
plt.title('Monte Carlo Drain Current Distribution Histogram')
plt.show()