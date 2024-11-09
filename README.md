# LTspice Monte Carlo Analysis Script
Run a Monte Carlo analysis in LTspice, und use this script to plot
your results. The scripts will return a distribution of the relative
frequency of your data, with the standard deviation and 3 sigma ranges 
shown on the plots.

### A few things to note:
- You have to enter the number of step of your monte carlo simulation in the script.
- You have to convert your output text file to a CSV file.
- Your spacing has to be the same in the CSV file (2 initial text rows, 4 identical data rows, one text row. repeated.)
- You have to have 2 data columns (voltage and current in this case) SEE CSV FILES USED FOR THIS SCRIPT
- You have to adjust the arrows spacing on the figures.
- The rest is automated.

### TODO:
- [x] Push initial scripts
- [ ] Update this to use a text file directly.
- [ ] Use functions for repetitive tasks.