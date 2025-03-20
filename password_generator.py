import re
import streamlit as st

#UI designing
st.set_page_config(page_title="Password strength Meter", page_icon="🌘", layout="centered")

#custom css
st.markdown(""" 
<style>
            .main{text-align: center;}
            .stTextInput{width:60% !imporatant; margin: auto;}
            .stButton button{width:20%; height:50px; background-color:#0892b8; color:white; font-size:20px; outline:none; border:none}
            .stButton button:hover {background-color:#1787a6; color:white; border-radius:20px; transition:1s ease}
</style>
""", unsafe_allow_html=True)

#page title and description

st.title("🔐 Password Strength Meter")

st.write("Enetr your password below to check security level....🔍")

#Function password strength

def password_strength(password):
    score=0
    feedback = []

    if len (password) >=8:
        score += 1 #increased score b y 1
    else:
        feedback.append("❌ Password should be **atleast 8 characters long**.")
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score +=1
    else:
        feedback.append("❌ Password should include **Both Upper Case and Lower Case**.")
    
    if re.search(r"\d", password):
        score +=1
    else:
        feedback.append("❌ Password should include **Atleast 1 number (0-9)**.")

#special Characters
    if re.search(r"[!@#$%^&*]", password):
        score +=1
    else:
        feedback.append("❌ Include **Atleast one special Character(!@$%^&*)**.")

#display password strength results
    if score == 4:
        st.success("✅ **Strong Password** Your Password is secure")
    elif score ==3:
        st.info("⚠️ **Moderate Password** Consider improving security by adding more features")
    else:
        st.error("❌ **Weak Password** follow the suggestion")

#feedback
    if feedback:
        with st.expander("🔍 **Improve your Password** "):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your Password:", type="password", help="Ensure Your password is strong 🔐" )

#Button 

if st.button("Check Strength"):
    if password:
        password_strength(password)
    else:
        st.warning("⚠️⚠️⚠️ Please input a password first!")#show warning if password is empty
    #.stButton button{width:20%; height:50px; background-color:#051f4b; color:white; font-size:18px;}
