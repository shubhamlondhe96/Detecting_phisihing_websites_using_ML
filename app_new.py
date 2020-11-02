import streamlit as st
import joblib
import os
os.getcwd()

model = joblib.load("Random_Forest_updated.pkl")




st.markdown(f'''<center><h1 style="font-family:cursive;color:rgb(0,250,200);text-decoration-line:overline underline;text-decoration-style:double ;">AIS Solutions Pvt Ltd.</h1></center>''',unsafe_allow_html=True)
st.markdown(f'''<center><h1 style="background-color:DodgerBlue ;">Detecting Phishing Website Using Machine Learning</h1><center>''',unsafe_allow_html=True)
# upload file where you have to test 


st.write("Select below option if response is Yes (or 1) ")

a5 = st.checkbox("Prefix_Suffix")

if a5:
	Prefix_Suffix = 1
else:
	Prefix_Suffix = 0

a11 = st.checkbox("URL_of_Anchor")

if a11:
	URL_of_Anchor = 1
else:
	URL_of_Anchor = 0


having_Sub_Domain	 = st.selectbox("having_Sub_Domain	", (0,1,2))

SSLfinal_State = st.selectbox("SSLfinal_State", (0,1,2))


Links_in_tags = st.selectbox("Links_in_tags", (0,1,2))


web_traffic = st.selectbox("web_traffic", (0,1,2))


lst = [SSLfinal_State,
 URL_of_Anchor,
 web_traffic,
 having_Sub_Domain,
 Links_in_tags,
 Prefix_Suffix]


if st.button("Predict"):
	x = model.predict([lst])[0]
	if x==1:
		st.header('Phishing')
	else:
		st.header('No Phishing')