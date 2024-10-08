from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the web driver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service('./chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a link to Reuters in a new tab
link_to_open = "https://www.reuters.com"
driver.execute_script(f"window.open('{link_to_open}', '_blank');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])

# Wait for the page to load
time.sleep(2)

# Perform actions in the new tab
print(f"Current URL: {driver.current_url}")

# Close the new tab
driver.close()

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])

# Close the driver
driver.quit()