import streamlit as st

col1,col2,col3,col4=st.columns((1,2,2,1))
with col2:
    st.markdown("### enter the number")
with col3:
    num=int(float(st.number_input("")))

for i in range(1,num):
    st.success(i)

