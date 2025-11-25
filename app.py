#import libraries
import pickle
import streamlit as st
import numpy as np

#load the model
with open("out.pickle","rb") as f:
    model=pickle.load(f)

#title of the app
st.header("Hello.We are here form predict your dream house price")
st.text("lets start. Give answer of some question")

#taking input of the app
rn=st.number_input("How many room you want:")
area=st.number_input("Your desired area of your house in sqft:")
bt=st.number_input("How many bathroom you want:")
b=[1,2,3]
bl=0
t=st.radio("Do you want any balcony",["Yes","No"])
if t=="Yes":
    t1=st.radio("How many balcony you want:",b)
    bl=t1
else:
    bl=0

#processing the data
x=np.array([[rn,area,bt,bl]])
y=model.predict(x)
y=y[0]

#showing output
if st.button("Submit"):
    st.success(f"Your house price will be {y} lakh")
    st.text("Note: this is just a prediction. It will not be always correct.")
