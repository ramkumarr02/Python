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

test = pd.read_csv("loan_test.csv")
test.head()


# Data Prep Function
# ########################################################################

def Data_prep(df):
    # Removing Loan Id and Loan Status for One-Hot encoding and Imputation
    # ########################################################
    predictors = df.columns
    predictors[1]
    predictors = np.delete(predictors,0)
    predictors = np.delete(predictors,-1)
    df[predictors]
    
    # One-Hot Encoding
    # ########################################################
    df_dummy = pd.get_dummies(df[predictors],dummy_na = True)
    df_dummy
    df_dummy.count()
    df_dummy.head()
    newcols = df_dummy.columns
    newcols
    
    # Data Imputations
    # ########################################################
    from fancyimpute import IterativeImputer
    df_imputed = IterativeImputer().fit_transform(df_dummy)
    df_imputed = pd.DataFrame(df_imputed,columns = newcols)
    df_imputed.head()
    df_imputed.count()

    return(df_imputed)
    
train_imputed = Data_prep(train)

# Adding Loan Id and Loan Status back again to Data
# ########################################################
train_imputed['Loan_Status'] = train['Loan_Status']
train_imputed.head()
train_imputed['Loan_Status'] = train_imputed.Loan_Status.map(dict(Y=1,N=0))
#train_imputed.to_csv("train_imputed.csv",sep=',')


test_imputed = Data_prep(test)

train_imputed.head()
test_imputed.head()

# Split DataFrame into Train and Test sets
# ########################################################
random_numbers = np.random.rand(len(train_imputed))<0.8
random_numbers

data_train = train_imputed[random_numbers]
data_test = train_imputed[~random_numbers]

data_train.count()
data_test.count()

predictors = data_train.columns
predictors = np.delete(predictors,-1)
target = data_train.columns[-1]

# Data Modelling
# ########################################################
from sklearn import linear_model

model = linear_model.LinearRegression()
model.fit(data_train[predictors],data_train[target])

model.coeff


from sklearn.metrics import mean_squared_error, r2_score

