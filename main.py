import streamlit as st 

st.image("logo.png")
st.title("Play with AI Models")
st.text("Play with some AI models that leverage GPU compuation, all running on the below server!")
st.button("Age Estimation",use_container_width=True)
st.button("Pose Estimation",use_container_width=True)
st.button("etc",use_container_width=True)

st.text("More Info")
col1, col2 = st.columns(2)
with col1:
    st.button("check out our webite!",use_container_width=True)
with col2: 
    st.button("book an appointment with our AI Hub Manager!",use_container_width=True)
