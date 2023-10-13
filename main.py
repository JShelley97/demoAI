import streamlit as st 
import webbrowser

st.image("logo.png")
st.title("Play with AI Models")
st.write("Play with some AI models that leverage GPU compuation, all running on the below server!")
st.button("Age Estimation",use_container_width=True)
st.button("Pose Estimation",use_container_width=True)
st.button("etc",use_container_width=True)

st.write("More Info")
col1, col2 = st.columns(2)
with col1:
    if st.button("check out our webite!",use_container_width=True):
        webbrowser.open_new_tab("https://lac2.org")
with col2: 
    if st.button("book an appointment with our AI Hub Manager!",use_container_width=True):
        webbrowser.open_new_tab("https://www.typecalendar.com/wp-content/uploads/2022/12/December-2023-Calendar.jpg")
    
