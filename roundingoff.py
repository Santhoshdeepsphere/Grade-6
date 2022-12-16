#Program to rounding off numbers
import streamlit as vAR_st
def roundup():
    def cleartext():
        vAR_st.session_state['Clear']=0
        vAR_st.session_state['Clear2']='Select'
    
    vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px;'></h1>", unsafe_allow_html=True)
    
    col1,col2= vAR_st.columns((2,2))
    
    with col1:
        vAR_st.write('')
        vAR_st.subheader("Enter the Number")
    
    with col2:
        num1=vAR_st.number_input('',key='Clear')
    
    with col1:
        vAR_st.write('')
        vAR_st.subheader("Rounding off to")
    
    with col2:
        category= vAR_st.selectbox('',('Select','Round up to the nearest 10s','Round up to the nearest 100s','Round up to the nearest 1000s'),key='Clear2')
    col3,col4,col5,col6=vAR_st.columns((5,2,2,5))

    with col4:
        vAR_st.write('')
        vAR_k=vAR_st.button("Submit",key='af')
    


    def tens(num1):
        vAR_rem = num1%10
        if vAR_rem < 5:
            num1=int(num1/10)*10
        else:
            num1=int((num1+10)/10)*10
        with col4:
            if vAR_k:
                vAR_st.write('')
                with col1:
                    vAR_st.subheader("Answer")
                with col2:
                    vAR_st.subheader(num1)  

    def hundreds(num1):
        vAR_rem = num1%100
        if vAR_rem < 50:
            num1=int(num1/100)*100
        else:
            num1=int((num1+100)/100)*100
        with col4:
            if vAR_k:
                vAR_st.write('')
                with col1:
                    vAR_st.subheader("Answer")
                with col2:
                    vAR_st.subheader(num1)

    def thousands(num1):
        vAR_rem=num1%1000
        if vAR_rem<500:
            num1 = int(num1/1000)*1000
        else:
            num1 = int((num1+1000)/1000)*1000
        with col4:
            if vAR_k:
                vAR_st.write('')
                with col1:
                    vAR_st.subheader("Answer")
                with col2:
                    vAR_st.subheader(num1)

    if category=='Round up to the nearest 10s':
        tens(num1)
        
    if category=='Round up to the nearest 100s':
        hundreds(num1)

    if category=='Round up to the nearest 1000s':
        thousands(num1)
    
        
    with col5:
        vAR_st.write('')
        vAR_st.button('Clear',on_click=cleartext)