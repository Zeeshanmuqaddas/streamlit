import streamlit as st

# Title
st.title("📘 Student Info Collector")

# Input fields
name = st.text_input("zahid meer:")
age = st.number_input("27:", min_value=1, max_value=100)
subject = st.selectbox("science:", ["Math", "Science", "English", "History", "Art"])

# Submit button
if st.button("Submit"):
    st.success("✅ Submission Successful!")
    st.write("### Student Details:")
    st.write(f"👤 Name: {name}")
    st.write(f"🎂 Age: {age}")
    st.write(f"📚 Favorite Subject: {subject}")
