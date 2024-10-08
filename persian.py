from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver service
service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)

# Open the DuckDuckGo homepage
url = "https://duckduckgo.com"
driver.get(url)

# Locate the search input field
search = driver.find_element(By.NAME, "q")

# Send the search query "Persian Cat" to the search input field
search.send_keys("Persian Cat")

# Optionally, you can submit the search by pressing Enter
search.submit()

# Wait for a few seconds to see the results
time.sleep(3)

# Close the browser
driver.close()