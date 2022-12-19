import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from title_1 import *
from img import *
with open('final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
#--------------------------------------Tables----------------------------------------------
def tables():
    image()
    st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Application to Tables</h1>", unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,1.5,1.8,6))
    with col1:
        st.markdown("")
        st.markdown("")
        st.write("# Enter the Number ")
    # ------to create the function to clear the input-------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
                st.session_state["text"] = ""
        st.button("Clear", on_click=clear_text) 
    # ---------input button----------#
    with col2:
        st.markdown("")
        vAR_input_number=st.text_input("",key="text")
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                st.markdown("")
                if vAR_input_number.isnumeric():
                    vAR_num=int(vAR_input_number)
                    for i in range(1,11):
                        st.write(vAR_num, "x", i, "=" ,vAR_num*i)
                else:
                    st.error("Error")
                with col1:
                    st.write("# Answer is ")