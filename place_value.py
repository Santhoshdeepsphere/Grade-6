import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from title_1 import *
from img import *
with open('final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
#-----------------------------------place values-------------------------------------------
def placevalues():
    image()
    st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Application to Place Values</h1>", unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,1.5,1.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Number ")
    with col2:
# ----input button-----#
        input_num=st.text_input("",key="text")
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["text"] = ""
        st.button("Clear", on_click=clear_text) 
    with bc1: 
        st.markdown("")
        st.markdown("")
    #----odd or even------#
        if st.button("Submit"):
            if input_num.isnumeric():
                input_num1=int(input_num)
                if len(input_num)==5:
                    ten_thousant = (input_num1 // 10000) % 10
                    thousand= (input_num1 // 1000) % 10
                    hundred= (input_num1 // 100) % 10
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        st.write("Ten Thousant",ten_thousant,"Thousand",thousand,"Hundred",hundred,"Tens",tens,"Units",units)
                elif len(input_num)==4:
                    thousand= (input_num1 // 1000) % 10
                    hundred= (input_num1 // 100) % 10
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        st.write("Thousand",thousand,"Hundred",hundred,"Tens",tens,"Units",units)
                elif len(input_num)==3:
                    hundred= (input_num1 // 100) % 10
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        st.write("Hundred",hundred,"Tens",tens,"Units",units)
                elif len(input_num)==2:
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        st.write("Tens",tens,"Units",units)
                elif len(input_num)==1:
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        st.write("Units",units)
                with col1:
                    st.write("# Answer is ")
            else:
                with col2:
                    st.error("Error")