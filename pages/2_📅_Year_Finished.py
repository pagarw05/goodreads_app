import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# NOTE: Import Plotly using: pip install plotly

st.set_page_config(page_title = "Year Finished", 
                   page_icon = "📅")

# Title and description
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Books Finished per Year</h2>
    """,
    unsafe_allow_html = True,
)

# Sidebar information
with st.sidebar:
    st.header("📅 Year Finished Instructions")
    st.write("""
    On this page, you can:
    1. View a bar chart showing the number of books you finished each year.
    2. Understand your most productive reading years.
    3. Identify trends in your reading habits over time.
    
    📊 **Tip**: Hover over the bars to see exact counts for each year.
    """)
    st.info("✅ Ensure your data includes a valid `Date Read` column for accurate results.")


if "user_data" in st.session_state:
    books_df = st.session_state["user_data"]

    # Year Finished
    books_df["Year Finished"] = pd.to_datetime(books_df["Date Read"]).dt.year
    books_per_year = books_df.groupby("Year Finished")["Book Id"].count().reset_index()
    books_per_year.columns = ["Year Finished", "Count"]

    # Bar chart using Plotly
    fig_year_finished = px.bar(books_per_year, 
                               x = "Year Finished", 
                               y = "Count", 
                               title = "Books Finished per Year",
                               color = "Count",
                               color_continuous_scale = "Sunset")
    # NOTE: For more colorscales: https://plotly.com/python/builtin-colorscales/
    fig_year_finished.update_xaxes(type = "category")
    st.plotly_chart(fig_year_finished)

    mode_year_finished = int(books_df["Year Finished"].mode()[0])
    st.write(f"**You finished the most books in {mode_year_finished}. Awesome job!**")
else:
    st.warning("⚠️ Please upload your Goodreads data on the 'Upload Data' page.")