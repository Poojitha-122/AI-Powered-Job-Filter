import pandas as pd
import streamlit as st

st.title("AI-Powered Job Filter")

uploaded_file = st.file_uploader("Upload a CSV file with job listings", type=["csv"])

# Scam check function
def check_scam(description):
    if pd.isnull(description):
        return "Legitimate"
    desc = description.lower()
    scam_keywords = ["registration fee", "advance", "pay", "deposit"]
    if any(word in desc for word in scam_keywords):
        return "Scam"
    return "Legitimate"

if uploaded_file is not None:
    jobs = pd.read_csv(uploaded_file)
    jobs["Status"] = jobs["Description"].apply(check_scam)
    st.write("### Filtered Jobs")
    st.dataframe(jobs)

    # Download filtered file
    csv = jobs.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download filtered CSV",
        data=csv,
        file_name='jobs_filtered.csv',
        mime='text/csv',
    )
