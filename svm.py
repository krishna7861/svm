import streamlit as st
import pickle
st.title("svm implementation app ")
age=st.number_input("enter the age")
sal=st.number_input("enter your salary")
 
button=st.button("predict")
if button:
    model=pickle.load(open("svm.pkl","rb"))
    res=model.predict([[age,sal]])[0]
    st.markdown(f"Predict svm Class :{res}")
