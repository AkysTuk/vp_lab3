from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Flask documentation")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert any("flask documentation" in result.text.lower() for result in results)
    driver.quit()

def test_google_multiple_keywords_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python tutorial Django tutorial")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    page_source_lower = driver.page_source.lower()
    assert "python tutorial" in page_source_lower
    assert "django tutorial" in page_source_lower
    driver.quit()

def test_google_tabs_filter():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Django tutorials")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Новини")
    driver.find_element(By.LINK_TEXT, "Зображення")
    driver.find_element(By.LINK_TEXT, "Відео")
    driver.quit()

def test_google_site_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("site:github.com Django")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.XPATH, "//h3/ancestor::a")
    for result in results:
        assert "github.com" in result.get_attribute("href").lower()
    driver.quit()

def test_google_intitle_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("intitle:Flask")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.XPATH, "//div[@id='search']//a/h3")
    for result in results:
        assert "flask" in result.text.lower()
    driver.quit()

def test_google_image_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.find_element(By.LINK_TEXT, "Зображення").click()
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("sunset")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    images = driver.find_elements(By.XPATH, "//div[@id='search']//h3/a//img")
    time.sleep(2)
    assert len(images) > 0
    driver.quit()

if __name__ == "__main__":
    test_google_search()
    test_google_multiple_keywords_search()
    test_google_tabs_filter()
    test_google_site_search()
    test_google_intitle_search()
    test_google_image_search()