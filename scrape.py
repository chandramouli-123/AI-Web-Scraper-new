from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    """Scrapes the given URL and returns the page content."""
    
    options = Options()
    options.add_argument("--headless")  # Run without opening a browser window
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(2)  # Allow page to load
        page_source = driver.page_source
        return page_source

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        driver.quit()


def extract_body_content(html_content):
    """Extracts the <body> content from the scraped HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""


def clean_body_content(body_content):
    """Removes unnecessary scripts, styles, and whitespace."""
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Remove <script> and <style> elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get cleaned text
    cleaned_text = soup.get_text(separator="\n")
    cleaned_text = "\n".join(line.strip() for line in cleaned_text.splitlines() if line.strip())

    return cleaned_text


def split_dom_content(dom_content, max_length=6000):
    """Splits the content into chunks to avoid overflow issues."""
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]
