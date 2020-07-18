# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:47:38 2020

@author: Faheem Ur Rehman
"""



import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("arsalan.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(DiabetesTypeOne,DiabetesTypeTwo,liverDisease
,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[DiabetesTypeOne,DiabetesTypeTwo,liverDisease
,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP]])
    print(prediction)
    return prediction



def main():
    st.title("IMS MEnu ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">IMS Menu ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    DiabetesTypeOne = st.checkbox("DiabetesTypeOne")
    if DiabetesTypeOne:
     st.checkbox("yes", value = True,key=0);
    DiabetesTypeTwo = st.checkbox("DiabetesTypeTwo")
    if DiabetesTypeTwo:
     st.checkbox("yes", value = True,key=1)
    liverDisease = st.checkbox("liverDisease")
    if liverDisease:
     st.checkbox("yes", value = True,key=2)
    heartDisease = st.checkbox("heartDisease")
    if heartDisease:
     st.checkbox("yes", value = True,key=3)
    kidneyDisease = st.checkbox("kidneyDisease")
    if kidneyDisease:
     st.checkbox("yes", value = True,key=4)
    Flu = st.checkbox("Flu")
    if Flu:
     st.checkbox("yes", value = True,key=5)
    Fever = st.checkbox("Fever" )
    if Fever:
     st.checkbox("yes", value = True,key=6)
    LowBP = st.checkbox("LowBP" )
    if LowBP:
     st.checkbox("yes", value = True,key=7)
    HighBP= st.checkbox("HighBP")
    if HighBP:
     st.checkbox("yes", value = True,key=8)
    result=""
    if st.button("Predict"):
      result=predict_note_authentication(DiabetesTypeOne,DiabetesTypeTwo,liverDisease,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP)
    st.success('The output is {}'.format(result)) 
   
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    