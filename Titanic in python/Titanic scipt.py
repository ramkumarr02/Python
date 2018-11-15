# Titanic Disaster Analyses
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

train = pd.read_csv("train.csv")
train.head()

test = pd.read_csv("test.csv")
test.head()
test.count()

from sklearn.linear_model import LogisticRegression


def modelling(model,data,pred_var,out_var):
    model.fit(data[pred_var],data[out_var])
    model
    
model = LogisticRegression()

predictor = ['Pclass']
outcome = ['Survived']

modelling(model, train, predictor,outcome)


