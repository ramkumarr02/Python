# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#%config IPCompleter.greedy = True

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

#import os
#print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

train = pd.read_csv("loan_train.csv")
train.head()

predictors = train.columns
predictors[1]
predictors = np.delete(predictors,0)
train[predictors]

train_dummy = pd.get_dummies(train[predictors],dummy_na = True)
train_dummy
train_dummy.count()
train_dummy.head()
newcols = train_dummy.columns
newcols

from fancyimpute import IterativeImputer
train_imputed = IterativeImputer().fit_transform(train_dummy)
train_imputed = pd.DataFrame(train_imputed,columns = newcols)
train_imputed.head()
train_imputed.count()

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
type(diabetes)

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]
type(diabetes_X)
len(diabetes_X)

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
len(diabetes_X_train)
len(diabetes_X_test)

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
len(diabetes.target)
len(diabetes_y_train)
len(diabetes_y_test)

diabetes.data_filename


