import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv(r"C:\Users\konth\Downloads\emp_sal.csv")
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values
#random tree
from sklearn.tree import DecisionTreeRegressor
dt_reg=DecisionTreeRegressor()
dt_reg.fit(x,y)
dt_pred=dt_reg.predict([[20]])
print(dt_pred)
#in random forest if we run code multiple times we will get different values as output because of ensemble concept
# to avoid that we are using random_state=0
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor()
rf_reg.fit(x,y)
rf_pred=rf_reg.predict([[6]])
print(rf_pred)