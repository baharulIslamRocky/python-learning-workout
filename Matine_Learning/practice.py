import pandas as pd
path='G:\MINE\SUB\Thesis\kaggle\melbourneHdata.csv'

data=pd.read_csv(path)
data=data.dropna(axis=0)
y=data.Price
feature=['Rooms', 'Bathroom', 'Landsize', 'BuildingArea','YearBuilt', 'Lattitude', 'Longtitude']
X=data[feature]

from sklearn.model_selection import train_test_split
train_x,val_x,train_y,val_y=train_test_split(X,y,random_state=0)

from sklearn.tree import DecisionTreeRegressor
dt_model=DecisionTreeRegressor(random_state=0)
maxDt_model= DecisionTreeRegressor(max_leaf_nodes=50,random_state=0)

dt_model.fit(train_x,train_y)
maxDt_model.fit(train_x,train_y)

pred=dt_model.predict(val_x)

from sklearn.metrics import mean_absolute_error
mae=mean_absolute_error(pred,val_y)
print("Normal Decision Tree MAE",mae)

pred=maxDt_model.predict(val_x)
mae=mean_absolute_error(val_y,pred)
print("Define Decision tree MAE:",mae)


from sklearn.ensemble import RandomForestRegressor
rf_model=RandomForestRegressor(random_state=0)
rf_model.fit(train_x,train_y)
pred=rf_model.predict(val_x)
print("Random Tree Regressor MAE:",mean_absolute_error(val_y,pred))
