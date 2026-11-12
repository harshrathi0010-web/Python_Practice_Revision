import streamlit as st

# set page config

st.set_page_config(page_title="Sara Analysis Dasboard",page_icon="🤖",layout="wide")

# header ,subheader and text

st.header("Sara Sales dashboard")

st.subheader("here we do all the analysis for profit")
st.text("starting from the data collection to the final depolyment")

# USEr input
num1=st.number_input("Enter the num1")
num2=st.number_input("Enter the num2")

if st.button("Addition"):
    st.subheader(num1+num2)


st.slider("Select age") # auto default value is 0 to 100
st.slider("select your physical age",0,25,9)

st.selectbox("Select your grade",["A","B","C","D"])


# KPI
st.metric("Total Sales",1043434)

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Total Sales",1043434,delta=1000)
with col2:
    st.metric("Total emp",1000,delta=-100)
with col3:
    st.metric("Total profit",100000,delta=10000)


st.radio("Select your gender",["Male","Female"])

