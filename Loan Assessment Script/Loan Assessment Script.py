# Loan Assessment Analyses
# ########################################################
# ########################################################

#Jupyter code
# ########################################################
#%config IPCompleter.greedy = True

# Kaggle Code
# ########################################################
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
#import os
#print(os.listdir("../input"))

# DataFrame creation
# ########################################################
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

train = pd.read_csv("loan_train.csv")
train.head()


# Removing Loan Id and Loan Status for One-Hot encoding and Imputation
# ########################################################
predictors = train.columns
predictors[1]
predictors = np.delete(predictors,0)
predictors = np.delete(predictors,-1)
train[predictors]

# One-Hot Encoding
# ########################################################
train_dummy = pd.get_dummies(train[predictors],dummy_na = True)
train_dummy
train_dummy.count()
train_dummy.head()
newcols = train_dummy.columns
newcols

# Data Imputations
# ########################################################
from fancyimpute import IterativeImputer
train_imputed = IterativeImputer().fit_transform(train_dummy)
train_imputed = pd.DataFrame(train_imputed,columns = newcols)
train_imputed.head()
train_imputed.count()

# Adding Loan Id and Loan Status back again to Data
# ########################################################
train_imputed['Loan_Status'] = train['Loan_Status']
train_imputed.head()
train_imputed['Loan_Status'] = train_imputed.Loan_Status.map(dict(Y=1,N=0))
#train_imputed.to_csv("train_imputed.csv",sep=',')

# Split DataFrame into Train and Test sets
# ########################################################
msk = np.random.rand(len(train_imputed))<0.8
msk

data_train = train_imputed[msk]
data_test = train_imputed[~msk]

data_train.count()
data_test.count()

# Data Modelling
# ########################################################
from sklearn import linear_model

model = linear_model.LinearRegression()

model.fit()


from sklearn.metrics import mean_squared_error, r2_score

