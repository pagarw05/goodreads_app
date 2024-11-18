import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Upload Data", 
                   page_icon = "📚")

# Title and description
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Upload Your Goodreads Data</h2>
    <p style = "text-align: center; font-size: 18px; color: #1c2d8f;">
    Start by uploading your Goodreads CSV file to unlock insights about your reading habits.
    </p>
    """,
    unsafe_allow_html = True,
)

# Sidebar information
with st.sidebar:
    st.header("📂 Upload Page Instructions")
    st.write("""
    On this page, you can:
    1. Upload your Goodreads **CSV file** exported from your account.
    2. Ensure the file contains valid data with columns like:
       - `Date Read`
       - `Date Added`
       - `Book Id`
       - `Exclusive Shelf`
       - `My Rating`
    3. Once uploaded, your data will be used across different analysis pages.
    """)
    st.info("📋 Tip: You can export your data from Goodreads under **Account Settings > Export Library**.")



# Add an expander for upload instructions
with st.expander("**How to export Goodreads data?** 📤"):
    st.write("""
    1. Go to your Goodreads account settings.
    2. Navigate to the **Export Library** section.
    3. Download the CSV file containing your reading data.
    4. Upload the file here to proceed.
    """)

# File uploader
uploaded_file = st.file_uploader(
    "Upload your Goodreads CSV file below 👇",
    help = "Ensure the file is in CSV format exported from Goodreads."
)

# Check if the file is uploaded
if uploaded_file is not None:
    # Read and save the uploaded data into session state
    df = pd.read_csv(uploaded_file)
    st.session_state["user_data"] = df

    # Display success message and preview
    st.success("File uploaded successfully!")
    st.write("Here's a preview of your data:")
    st.dataframe(df.head(), use_container_width = True)
    
    # Calculate statistics
    total_books = df['Book Id'].nunique()
    rated_books = df[df['My Rating'] != 0].shape[0]
    avg_pages = df['Number of Pages'].mean().round()
    most_read_author = df['Author'].mode()[0]
    
    # Display quick summary
    st.markdown("### Quick Stats:")
    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"⭐ **Books Rated:** {rated_books}")
    st.write(f"📖 **Average Pages per Book:** {avg_pages}")
    st.write(f"👨‍💻 **Most Read Author:** {most_read_author}")
    
else:
    st.warning("Please upload your Goodreads data to proceed.")



