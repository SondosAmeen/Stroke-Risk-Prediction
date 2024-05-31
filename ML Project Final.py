# Import necessary libraries.
import streamlit as st 
import pickle
import pandas as pd 
import sklearn

st.title("Stroke Occurence prediction")
st.info("Please fill out the sections below")
st.sidebar.header("Occurence")

# Load the downloaded sav file onto the model.
dtree1=pickle.load(open(r"C:\Users\20106\Downloads\Machine Learning\Strokesdataset_2.sav",'rb'))

# Create text input fields.
gender=st.text_input('Gender (Male = 0, Female = 1)')
age=st.text_input('Age')
hypertension=st.text_input('Hypertension (True = 1, False = 0)')
heart_disease=st.text_input('Heart Diseases (True = 1, False = 0)')
ever_married=st.text_input('Marital Status (True = 1, False = 0)')
Residence_type=st.text_input('Residence Status (Rural = 0, Urban = 1)')
avg_glucose_level=st.text_input('Average Glucose Level')
bmi=st.text_input('Body Mass Index')


# Create a dataframe and add everything to it. 
dataset_new=pd.DataFrame({'Gender (Male = 0, Female = 1)':[gender],'Age':[age],
'Hypertension (True = 1, False = 0)':[hypertension], 'Heart Diseases (True = 1, False = 0)':[heart_disease],
'Marital Status (True = 1, False = 0)':[ever_married],'Residence Status (Rural = 0, Urban = 1)':[Residence_type],
'Average Glucose Level':[avg_glucose_level],'Body Mass Index':[bmi]},index=[0])

Confirm_button=st.sidebar.button('Confirm')
if Confirm_button:
    result=dtree1.predict(dataset_new)
    if result == 0:
        st.sidebar.write('No Stroke')
        
    else:
        st.sidebar.write('Stroke')
    st.sidebar.image('https://blog.uvahealth.com/wp-content/uploads/2022/10/stroke-causes-graphic.jpg',width=250)
