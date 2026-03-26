from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_visible_text_from_url(url: str) -> str:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        return driver.find_element("tag name", "body").text
    finally:
        driver.quit()