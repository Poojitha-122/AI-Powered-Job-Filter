import streamlit as st
import pandas as pd

st.title("AI-Powered Job Filter")
st.write("Upload a CSV file with job listings to detect possible scam posts.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# --- function to check scam ---
def check_scam(text: str) -> str:
    """
    Very simple rule-based filter.
    You can expand with ML later.
    """
    scam_keywords = [
        "registration fee",
        "advance payment",
        "pay fee",
        "processing fee",
        "upfront"
    ]
    text_lower = str(text).lower()
    for kw in scam_keywords:
        if kw in text_lower:
            return "Scam"
    return "Legitimate"

if uploaded_file is not None:
    # Read the CSV
    jobs = pd.read_csv(uploaded_file)

    # Show column names for debugging
    st.write("Detected columns:", list(jobs.columns))

    # Try to find description column automatically
    desc_col = None
    for col in jobs.columns:
        if "desc" in col.lower():  # e.g. Description, Job Description
            desc_col = col
            break

    if desc_col is None:
        st.error("Could not find a description column. Please make sure your CSV has a column with 'Description' in its name.")
    else:
        jobs["Status"] = jobs[desc_col].apply(check_scam)
        st.subheader("Filtered Jobs")
        st.dataframe(jobs)

        # Optionally allow download of the filtered CSV
        csv_out = jobs.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download filtered CSV",
            data=csv_out,
            file_name="jobs_filtered.csv",
            mime="text/csv"
        )
else:
    st.info("Please upload a CSV file.")

