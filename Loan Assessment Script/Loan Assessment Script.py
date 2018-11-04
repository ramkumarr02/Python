# -*- coding: utf-8 -*-
"""
Loan Assessment
"""

import numpy as np
import pandas as pd

train = pd.read_csv("loan_train.csv")
print(train.head(5))
print(train.describe())

predictors = train.columns.values
print(predictors)
predictors = np.delete(predictors,0)


train.count()



train_dummy = pd.get_dummies(train,dummy_na=True)

train_dummy.count()