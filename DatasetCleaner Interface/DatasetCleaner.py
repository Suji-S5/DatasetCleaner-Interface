import streamlit as st
import pandas as pd
#page setup
st.set_page_config(page_title="Dataset Cleaner",layout="centered",initial_sidebar_state="expanded")
#css styles applied
st.markdown(
    """
<style>
body{
background-color:#fce4ec;
}
.stApp{
background-color:#ffffff;
padding:20px;
border-radius:10px;
}
h1{
color:#ff4b4b;
}
.stButton>button{
background-color:#ff4b4b;
color:white;
}
</style>
""",
unsafe_allow_html=True
)
#sidebar
st.sidebar.title("Navigation")
st.sidebar.info("Use this tool to clean and preview your CSV dataset.")
# Main Title
st.title("Dataset Cleaner Interface")
#file upload section
st.subheader("1.Upload Your CSV file")
file=st.file_uploader("Choose a CSV file", type="csv")
#if file is uploaded
if file is not None:
    data=pd.read_csv(file)
    st.subheader("2.preview of the Data")
    st.dataframe(data.head())
    st.subheader("3.Dataset Info")
    st.write(f"Number of Rows:'{data.shape[0]}'")
    st.write(f"Number of Columns:'{data.shape[1]}'")
    st.subheader("4.Check for Issues")
    #missing Values
    missing_data=data.isnull().sum()
    missing_data=missing_data[missing_data>0]
    if not missing_data.empty:
        st.warning("Missing Values Found")
        st.write(missing_data)
    else:
        st.success("No missing values!")
    #Duplicate Rows
    dup_count=data.duplicated().sum()
    if dup_count>0:
        st.warning(f"{dup_count}duplicate rows found")
    else:
        st.success("No duplicates!")
    #Data Types
    st.subheader("5.Data Types")
    st.write(data.dtypes)
    #Clean and Download
    if st.button("Clean and Download"):
        cleaned_data=data.drop_duplicates().dropna()
        st.success("Dataset cleaned successfully.")
        st.download_button("Download Cleaned File",cleaned_data.to_csv(index=False),"cleaned_dataset.csv","text/csv")
    st.markdown(
            """
        <hr style="margin-top:30px;"><small>Developed by SUJI S</small>""",unsafe_allow_html=True
        )