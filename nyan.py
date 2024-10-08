from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)

# Open YouTube
driver.get("https://www.youtube.com")

# Wait for the page to load
time.sleep(2)

# Find the search bar and enter "Nyan Cat"
search_bar = driver.find_element(By.NAME, "search_query")
search_bar.send_keys("Nyan Cat")

# Submit the search query
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

# Find and click on the first video result
first_video = driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer.ytd-item-section-renderer #thumbnail")
first_video.click()

# Wait for the video to load and play
time.sleep(90)  # Adjust the sleep time as needed

# Close the browser
driver.close()