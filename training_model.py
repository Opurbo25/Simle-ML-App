#install essential libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

#load csv file
df=pd.read_csv("price.csv")

#making two dataframe
x=df[["size","total_sqft","bath","balcony"]]
y=df.price


#clean the size column
def fun(x):
  x=str(x)
  t=x.split(" ")
  return t[0]
x["size"]=x["size"].apply(fun)

#filling null value of bath column  with mean and balcony column with 0
a=x["bath"].mean()
x["bath"]=x["bath"].fillna(int(a))
x["balcony"]=x["balcony"].fillna(0)

#filling null value of total_sqft column  with mean
x["total_sqft"]=pd.to_numeric(x["total_sqft"],errors="coerce")
x["total_sqft"]=x["total_sqft"].fillna(x["total_sqft"].mean())

#filling null value of size columns
x["size"]=pd.to_numeric(x["size"],errors="coerce")
b=x["size"].mean()
b=int(b)
x["size"]=x["size"].fillna(b)

#rename the columns's name
x=x.rename(columns={"size":"room","total_sqft":"area"})

#Training a model with linear regression
model=LinearRegression()
model.fit(x,y)

#making out.pickle file with this model
f="out.pickle"
with open(f,"wb") as fi:
  pickle.dump(model,fi)
