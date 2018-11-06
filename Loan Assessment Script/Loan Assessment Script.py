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
predictors = np.delete(predictors,-1)
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


train_imputed['Loan_Status'] = train['Loan_Status']
train_imputed.head()
train_imputed['Loan_Status'] = train_imputed.Loan_Status.map(dict(Y=1,N=0))
#train_imputed.to_csv("train_imputed.csv",sep=',')

# Data split
#msk = np.random.rand(len(train_imputed))<0.8
np.random.rand(len(train_imputed)).count()

