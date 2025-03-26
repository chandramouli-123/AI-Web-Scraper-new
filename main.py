import streamlit as st
from scrape import scrape_website

# Streamlit App Title
st.title("AI Web Scraper")

# User Input: Website URL
url = st.text_input("Enter a Website URL:")

# Scrape Button
if st.button("Scrape Site"):
    if url.strip():  # Ensure the URL is not empty
        with st.spinner("Scraping the website... Please wait!"):
            result = scrape_website(url)
        st.success("Scraping Complete!")
        st.write(result)
    else:
        st.warning("Please enter a valid URL before scraping.")
