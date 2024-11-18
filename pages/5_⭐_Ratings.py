import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title = "Ratings", 
                   page_icon = "⭐")

# Title and description
st.markdown(
    """
    <h2 style = "text-align: center; color: #DECAAF;">Ratings Analysis</h2>
    """,
    unsafe_allow_html = True,
)

# Sidebar information
with st.sidebar:
    st.header("⭐ Ratings Analysis")
    st.write("""
    On this page, you can:
    1. View the distribution of your personal ratings.
    2. Explore the distribution of Goodreads' average ratings.
    3. Compare your ratings with Goodreads' averages to see how they align or differ.

    📊 **Tip**:
    - Hover over the bars in the charts to see exact values.
    """)
    st.info("✅ Ensure your data includes valid `My Rating` and `Average Rating` columns for accurate analysis.")


if "user_data" in st.session_state:
    books_df = st.session_state["user_data"]

    # Filter books with non-zero ratings
    books_rated = books_df[books_df["My Rating"] != 0]

    # My Rating Histogram
    fig_my_rating = px.histogram(
        books_rated,
        x = "My Rating",
        title = "Distribution of My Ratings",
        nbins = 5,
        labels = {"My Rating": "My Rating (Stars)"},
        color_discrete_sequence = ["#FFA07A"]
    )
    fig_my_rating.update_layout(
        yaxis = dict(title = "Number of Books"),
    )

    # Average Goodreads Rating Histogram
    fig_avg_rating = px.histogram(
        books_rated,
        x = "Average Rating",
        title = "Distribution of Goodreads Average Ratings",
        nbins = 10,
        labels = {"Average Rating": "Average Rating (Stars)"},
        color_discrete_sequence = ["#87CEEB"]
    )
    fig_avg_rating.update_layout(
        yaxis = dict(title = "Number of Books")
    )

    # Display the plots
    st.plotly_chart(fig_my_rating)
    avg_my_rating = round(books_rated["My Rating"].mean(), 2)
    st.write(f"⭐ You rate books an average of **{avg_my_rating} stars**.")

    st.plotly_chart(fig_avg_rating)
    avg_difference = np.round(np.mean(books_rated["My Rating"] - books_rated["Average Rating"]), 2)
    sign = "higher" if avg_difference >= 0 else "lower"
    st.write(f"📊 You rate books **{sign} than the average Goodreads user** by **{abs(avg_difference)} stars**!")
else:
    st.warning("⚠️ Please upload your Goodreads data on the 'Upload Data' page.")
