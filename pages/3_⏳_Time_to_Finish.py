import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# NOTE: Import Plotly using: pip install plotly

st.set_page_config(page_title = "Time to Finish", 
                   page_icon = "⏳")

# Title and description
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Time to Finish Books</h2>
    """,
    unsafe_allow_html = True,
)

# Sidebar information
with st.sidebar:
    st.header("⏳ Time to Finish Instructions")
    st.write("""
    On this page, you can:
    1. Explore a histogram showing how long it took you to finish books after adding them to Goodreads.
    2. Analyze trends in your reading habits and efficiency over time.
    3. Gain insights into how quickly you typically read books.

    📊 **Tip**: Hover over the bars to see the exact number of books finished within a given time range.
    """)
    st.info("✅ Ensure your data includes both `Date Added` and `Date Read` columns for accurate calculations.")


if "user_data" in st.session_state:
    books_df = st.session_state["user_data"]

    # Time Difference
    books_df["days_to_finish"] = (pd.to_datetime(books_df["Date Read"]) - pd.to_datetime(books_df["Date Added"])).dt.days
    books_finished_filtered = books_df[(books_df["Exclusive Shelf"] == "read") & (books_df["days_to_finish"] >= 0)]

    # Histogram using Plotly
    fig_days_finished = px.histogram(
        books_finished_filtered,
        x = "days_to_finish",
        title = "Time Between Date Added and Date Finished",
        labels = {"days_to_finish": "Days"},
        nbins = 20
    )
    # Set a uniform color for bins 
    fig_days_finished.update_traces(marker_color = "#7d5abc")

    st.plotly_chart(fig_days_finished)

    mean_days_to_finish = int(books_finished_filtered["days_to_finish"].mean())
    st.write(f"**It took you an average of {mean_days_to_finish} days between when the book was added to Goodreads and when you finished the book.**")
else:
    st.warning("⚠️ Please upload your Goodreads data on the 'Upload Data' page.")