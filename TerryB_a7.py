from scipy import stats
from scipy.stats import skewtest, kurtosistest
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
from statistics import median
import statsmodels.api as sm
plt.close('all')


######################################################################
# Ben Terry
# Data Science & Analytics
######################################################################

###### VARIABLES ######
alpha = .05
cut = 125

################ PART A ################
print('\n'*25)
print("##################################")
print('Output from application TerryB_a7.py')
print('Developed by Ben Terry')
print("##################################\n")

# Read the data file and assign Series object
print('\nInitiating scrubbing for part A...')
datfile='C:\\Users\\ben_i\\Documents\\2019_Public_Data_File_-_Students.csv'

frame = pd.read_csv(datfile, low_memory = False)

count = len(frame) # ROW COUNT


# 1. Drop unwanted columns
frame.drop(frame.columns.difference(['Effective School Leadership Score', 'Collaborative Teachers Score']),
           1, inplace = True)


# 2. Drop any empty rows that might now exist in the dataframe
frame.dropna(how='all', inplace=True)


# Perform normaltest() check
print('\nChecking for normality...')
leader = stats.normaltest(frame['Effective School Leadership Score'])
teacher = stats.normaltest(frame['Collaborative Teachers Score'])

print('\nNormal test for Effective School Leadership Score:', '\nt-statistic -', 
      format(leader[0], '.3f'), '    p-val - ', leader[1])
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(teacher[0], '.3f'),'     p-val -', teacher[1])

print('\nResults show that the distribution is non-normal. Transformation and truncation needed.')


# Transform
print('\n\nApplying transformation...')

frame = frame.transform(lambda x: x**2)


# Truncate majority of the transformed rows in the dataframe and only save the first 125 rows 
print('\nApplying truncation...')

frame = frame.iloc[0:cut,:]


# 4. Reapply normal tests
leader = stats.normaltest(frame['Effective School Leadership Score'])
teacher = stats.normaltest(frame['Collaborative Teachers Score'])

print('\nNormal test for Effective School Leadership Score:', '\nt-statistic -', 
      format(leader[0], '.3f'), '    p-val - ', format(leader[1], '.3f'))
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(teacher[0], '.3f'),'     p-val -', format(teacher[1], '.3f'))

print('\nResults show that the distribution is now normal. Parametric techniques can be used for further analysis!')


# 5. Display scatter plot for 'eye check'
plt.scatter(frame['Effective School Leadership Score'],
            frame['Collaborative Teachers Score'], c = 'Red', alpha = 1)

print('\nA scatter plot is available for analysis.')


# Bartlett() test to check variances
bartlett = stats.bartlett(leader, teacher)

print('\n\nChecking variances...\n')
print('Bartlett() test results:\n')
print('Test statistic:', format(bartlett[0], '.2f'), '\nP-value =', format(bartlett[1], '.3f'))
print('\nResults are non-significant which confirm homogeneity.\n')

print('\n######## Scrubbing has been completed! ########\n')
print('Size before scrubbing:', count)
print('Size after scrubbing:', len(frame))
print('Data is now prepared for Part A regression analysis.')


# Part A analysis

# 7. Stage data for use by statsmodels.OLS()
X = frame[['Effective School Leadership Score']] # Frame
Y = frame['Collaborative Teachers Score'] # Series


# 8. prepend an entry to the X values dataframe to represent the constant 
# term that will be needed for the regression equation

    # Adds a constant term (new column, value 1) to all rows of
    # the predictor DataFrame X and assigns the result to a new dataframe

X = sm.add_constant(X) # add constant for modeling


# 9. Create and train (fit) the model using OLS regression from statsmodels
model = sm.OLS(Y, X).fit()


# 10. The trained or fitted model must next be exercised to determine it’s accuracy,
# predictive significance, etc.

# Run the model to see how well it predicts the dependent variable (Y) values
predictions = model.predict(X)


print('\nApplying regression analysis...\n')
pmodel = model.summary()
#print(pmodel)

print('\nResults show that the regression model was significantly predictive:\n',
      'f =', model.fvalue, 'p =', model.f_pvalue)

print("\nIn the variable 'Collaborative Teachers Score', the regression model illustrates", 
      format(model.rsquared * 100, '.2f'), '%', 'of adjusted variance.')

print('\nRegression Coefficients')
print('-----------------------------------')
print('const:'.ljust(34), model.params[0], '       significance:', model.pvalues[0])
print('Effective School Leadership Score:', model.params[1], '      significance:', model.pvalues[1])
print("\nThese are the elements that significantly predicted the 'Collaborative Teachers Score'.")


#print(model.fvalue, '\n', model.f_pvalue, '\n', model.rsquared, '\n', model.rsquared_adj, '\n', model.params, '\n', model.pvalues)


################ PART B ################
print('\n\nInitiating scrubbing for part B...')
datfile='C:\\Users\\ben_i\\Documents\\2019_Public_Data_File_-_Students.csv'

frame2 = pd.read_csv(datfile, low_memory = False)

count = len(frame2) # ROW COUNT


# 1. Drop unwanted columns
frame2.drop(frame2.columns.difference(['Effective School Leadership Score', 'Collaborative Teachers Score', 
                                     'Rigorous Instruction Score', 'Trust Score']), 1, inplace = True)


# 2. Drop any empty rows that might now exist in the dataframe
frame2.dropna(subset = ['Effective School Leadership Score',
                        'Collaborative Teachers Score', 
                        'Rigorous Instruction Score', 
                        'Trust Score'], inplace = True)

# Perform normaltest() check
print('\nChecking for normality...')
leader = stats.normaltest(frame2['Effective School Leadership Score'])
teacher = stats.normaltest(frame2['Collaborative Teachers Score'])
iScore = stats.normaltest(frame2['Rigorous Instruction Score'])
tScore = stats.normaltest(frame2['Trust Score'])

print('\nNormal test for Effective School Leadership Score:', '\nt-statistic -', 
      format(leader[0], '.3f'), '    p-val - ', leader[1])
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(teacher[0], '.3f'),'     p-val -', teacher[1])
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(iScore[0], '.3f'),'     p-val -', iScore[1])
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(tScore[0], '.3f'),'     p-val -', tScore[1])


print('\nResults show that the distributions is non-normal. Transformation and truncation needed.')


# Transform
print('\n\nApplying transformation...')

frame2 = frame2.transform(lambda x: x**2)


# Truncate majority of the transformed rows in the dataframe and only save the first 125 rows 
print('\nApplying truncation...')

frame2 = frame2.iloc[0:cut,:]


# 4. Reapply normal tests
leader = stats.normaltest(frame2['Effective School Leadership Score'])
teacher = stats.normaltest(frame2['Collaborative Teachers Score'])
iScore = stats.normaltest(frame2['Rigorous Instruction Score'])
tScore = stats.normaltest(frame2['Trust Score'])

print('\nNormal test for Effective School Leadership Score:', '\nt-statistic -', 
      format(leader[0], '.3f'), '    p-val - ', leader[1])
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(teacher[0], '.3f'),'     p-val -', teacher[1])
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(iScore[0], '.3f'),'     p-val -', iScore[1])
print('\nCollaborative Techers Score:', '\nt-statistic -',
      format(tScore[0], '.3f'),'     p-val -', tScore[1])

print('\nResults show that the distributions are now normal. Parametric techniques can be used for further analysis!')


# 5. Display scatter plots for 'eye check'
plt.scatter(frame2['Effective School Leadership Score'],
            frame2['Collaborative Teachers Score'], c = 'Red', alpha = 1)

plt.scatter(frame2['Rigorous Instruction Score'],
            frame2['Collaborative Teachers Score'], c = 'Blue', alpha = 1)

plt.scatter(frame2['Trust Score'],
            frame2['Collaborative Teachers Score'], c = 'Green', alpha = 1)


print('\nA scatter plot is available for analysis.')


# Bartlett() test to check variances
bartlett = stats.bartlett(leader, teacher, iScore, tScore)

print('\n\nChecking variances...\n')
print('Bartlett() test results:\n')
print('Test statistic:', format(bartlett[0], '.2f'), '\nP-value =', format(bartlett[1], '.3f'))
print('\nResults are non-significant which confirm homogeneity.\n')

print('\n######## Scrubbing has been completed! ########\n')
print('Size before scrubbing:', count)
print('Size after scrubbing:', len(frame2))
print('Data is now prepared for Part B regression analysis.')


# Part A analysis

# 7. Stage data for use by statsmodels.OLS()
X = frame2[['Effective School Leadership Score', 
           'Rigorous Instruction Score', 'Trust Score']]

Y = frame2['Collaborative Teachers Score']


# 8. prepend an entry to the X values dataframe to represent the constant 
# term that will be needed for the regression equation

    # Adds a constant term (new column, value 1) to all rows of
    # the predictor DataFrame X and assigns the result to a new dataframe

X = sm.add_constant(X) # add constant for modeling


# 9. Create and train (fit) the model using OLS regression from statsmodels
model = sm.OLS(Y, X).fit()


# 10. The trained or fitted model must next be exercised to determine it’s accuracy,
# predictive significance, etc.

# Run the model to see how well it predicts the dependent variable (Y) values
predictions = model.predict(X)


print('\nApplying regression analysis...\n')


print('\nResults show that the regression model was significantly predictive:\n',
      'f =', model.fvalue, 'p =', model.f_pvalue)

print("\nIn the variable 'Collaborative Teachers Score', the regression model illustrates", 
      format(model.rsquared * 100, '.2f'), '%', 'of adjusted variance.')

print('\nRegression Coefficients')
print('-----------------------------------')
print('const:'.ljust(34), model.params[0], '       significance:', model.pvalues[0])
print('Trust Score:'.ljust(34), model.params[3], '       significance:', model.pvalues[3])
print('Rgorous Instruction Score:'.ljust(34), model.params[2], '       significance:', model.pvalues[2])
print('Effective School Leadership Score:'.ljust(34), model.params[1], '      significance:', model.pvalues[1])
print("\nThese are the elements that significantly predicted the 'Collaborative Teachers Score'.")


print('\n\n############### End of Application ###############')











































