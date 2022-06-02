# Data-Science-Analytics-Students
Pandas dataframe analysis on school's ability to support student success - scrubs, filters, and runs data analysis tests.

# Output From Application TerryB_a7.py - Developed by Ben Terry


Initiating scrubbing for part A...

Checking for normality...

Normal test for Effective School Leadership Score: <br />
t-statistic - 69.290  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; p-val -  8.99232139504058e-16

Collaborative Techers Score: <br />
t-statistic - 29.237    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  p-val - 4.4797253445195697e-07

Results show that the distribution is non-normal. Transformation and truncation needed.<br /><br />


Applying transformation...

Applying truncation...

Normal test for Effective School Leadership Score: <br />
t-statistic - 2.886   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  p-val -  0.236

Collaborative Techers Score: <br />
t-statistic - 4.043   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val - 0.132

Results show that the distribution is now normal. Parametric techniques can be used for further analysis!<br />

A scatter plot is available for analysis.<br /><br />
![img](https://www.linkpicture.com/q/Figure-2022-06-02-012616.png)<br /><br />

Checking variances...

Bartlett() test results:

Test statistic: 0.10 <br />
P-value = 0.754

Results are non-significant which confirm homogeneity.<br /><br />


######## Scrubbing has been completed! ########

Size before scrubbing: 1829<br />
Size after scrubbing: 125<br />
Data is now prepared for Part A regression analysis.

Applying regression analysis...


Results show that the regression model was significantly predictive:<br />
f = 95.50918176236797 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; p = 4.822019240499686e-17

In the variable 'Collaborative Teachers Score', the regression model illustrates 43.71 % of adjusted variance.

Regression Coefficients
-----------------------------------
const:                             5.063143981774277<br />        significance: 4.409875745304627e-06<br /><br />
Effective School Leadership Score: 0.7111000230014979<br />       significance: 4.822019240499566e-17

These are the elements that significantly predicted the 'Collaborative Teachers Score'.<br /><br />


Initiating scrubbing for part B...

Checking for normality...

Normal test for Effective School Leadership Score: <br />
t-statistic - 67.551   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  p-val -  2.1454343503445025e-15

Collaborative Techers Score: <br />
t-statistic - 31.911   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val - 1.1763471877212416e-07

Collaborative Techers Score: <br />
t-statistic - 39.874   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val - 2.195282498403507e-09

Collaborative Techers Score: <br />
t-statistic - 84.614   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val - 4.228642216212558e-19

Results show that the distributions is non-normal. Transformation and truncation needed.<br /><br />


Applying transformation...

Applying truncation...

Normal test for Effective School Leadership Score: <br />
t-statistic - 3.137  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val -  0.2083718151969694

Collaborative Techers Score: <br />
t-statistic - 4.720   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val - 0.09443046789539254

Collaborative Techers Score: <br />
t-statistic - 4.496   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val - 0.10562521336387172

Collaborative Techers Score: <br />
t-statistic - 4.289   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   p-val - 0.1171489166084221

Results show that the distributions are now normal. Parametric techniques can be used for further analysis!

A scatter plot is available for analysis.<br /><br />
![img](https://www.linkpicture.com/q/Scatter-Plot-2.png)<br /><br />


Checking variances...

Bartlett() test results:

Test statistic: 0.16 <br />
P-value = 0.984

Results are non-significant which confirm homogeneity.<br /><br />


######## Scrubbing has been completed! ########

Size before scrubbing: 1829<br />
Size after scrubbing: 125<br />
Data is now prepared for Part B regression analysis.<br /><br />

Applying regression analysis...


Results show that the regression model was significantly predictive:<br />
 f = 109.16287304356094 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; p = 2.861440325971643e-34

In the variable 'Collaborative Teachers Score', the regression model illustrates 73.02 % of adjusted variance.

Regression Coefficients
-----------------------------------
const:                             0.875568108748453<br />        significance: 0.2900907396170457<br /><br />
Trust Score:                       0.35614770691386105<br />        significance: 3.271468208972591e-06<br /><br />
Rgorous Instruction Score:         0.4307710773513167<br />        significance: 2.2253091621574742e-15<br /><br />
Effective School Leadership Score: 0.19397249398642077<br />       significance: 0.013613022743028029<br />

These are the elements that significantly predicted the 'Collaborative Teachers Score'.


############### End of Application ###############
