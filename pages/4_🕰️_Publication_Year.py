import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# NOTE: Import Plotly using: pip install plotly

st.set_page_config(page_title = "Publication Year", 
                   page_icon = "🕰️")

# Title and description
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Publication Year Analysis</h2>
    """,
    unsafe_allow_html = True,
)

# Sidebar information
with st.sidebar:
    st.header("📆 Publication Year Instructions")
    st.write("""
    On this page, you can:
    1. View a bar chart showing the number of books published in different years.
    2. Analyze trends in the publication years of books you've read.
    3. Discover how your reading preferences align with historical trends.

    📊 **Tip**: Hover over the bars to see exact counts for each year.
    """)
    st.info("✅ Ensure your data includes a valid `Original Publication Year` column.")

if "user_data" in st.session_state:
    books_df = st.session_state["user_data"]

    # Publication Year
    books_publication_year = books_df.groupby("Original Publication Year")["Book Id"].count().reset_index()
    books_publication_year.columns = ["Year Published", "Count"]

    fig_year_published = px.bar(
        books_publication_year, 
        x = "Year Published", 
        y = "Count", 
        title = "Book Age Plot",
        color = "Count",
        color_continuous_scale = "Peach")
    fig_year_published.update_xaxes(range = [1850, 2021])
    st.plotly_chart(fig_year_published)

    st.write("This chart is zoomed into the period of 1850-2021, but is interactive, so try zooming in/out on interesting periods!")
else:
    st.warning("⚠️ Please upload your Goodreads data on the 'Upload Data' page.")
