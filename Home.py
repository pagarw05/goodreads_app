import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "👋",
    # layout = "wide"
)

# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style = "text-align: center; color: #DECAAF;">Goodreads: Analysis of Reading Habits</h2>
    """,
    unsafe_allow_html = True,
)

# Subtitle with styling
st.markdown(
    """
    <h3 style = "text-align: center; color: #D6AAFF; font-family: Arial, sans-serif;">
    Discover insights about your reading habits, favorite authors, and much more!
    </h3>
    """,
    unsafe_allow_html = True,
)

# Insert an image
st.image("goodreads_image.jpg", 
         caption = "Uncover trends and patterns in your reading journey!", 
         use_column_width = True)

# Sidebar navigation header
with st.sidebar:
    st.header("🔍 Navigate the App")
    st.write("Use the links above to explore:")
    st.markdown("""
    - **Upload Data**: Upload your Goodreads CSV file.
    - **Year Finished**: Analyze books finished per year.
    - **Time to Finish**: Explore reading time trends.
    - **Other Pages**: Discover more insights.
    """)

st.sidebar.info("Select a task above to proceed.")

# Interactive introduction with expander
with st.expander("**What can you do with this app?**"):
    st.write("""
    📚 **Upload your Goodreads Data**: Start by uploading your exported Goodreads CSV file.
    
    📊 **Visualize Your Reading Trends**: Discover patterns like:
    - Books read per year
    - Average time to finish a book
    - Book length distribution
    - Your most-read authors and genres

    🌟 **Compare Ratings**: See how your ratings compare to Goodreads' averages.

    🛠️ **Interactive Features**: All charts are fully interactive. Zoom in, filter data, and explore trends!
    """)
        
# Add a footer
st.markdown(
    """
    <hr>
    <p style = "text-align: center; color: #777; font-size: 14px; font-family: Arial, sans-serif;">
    Made with ❤️ for book lovers.
    </p>
    """,
    unsafe_allow_html = True,
)