import streamlit as st
import streamlit.components.v1 as components
import json 

from supabase import create_client, Client

st.title("Health Portal")   

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()


def magic_link(email):
   response = supabase.auth.sign_in_with_otp({'email': email})
   if response:
     st.success("check your email address for login link")
   else:   
     st.warning("enter a valid email address or phone number") 





col1 = st.columns()
with col1:
        with st.expander('Generate Magic Link'):
            email = st.text_input('Email', key='enter email address')
            generate_btn = st.button('Generate Magic Link', on_click=magic_link, args=(email))
                                     


