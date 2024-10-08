from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up Chrome options (optional)
chrome_options = Options()
# Remove headless mode to see the browser window
# chrome_options.add_argument("--headless")

# Set up the WebDriver (specify the path to your ChromeDriver if not in PATH)
service = Service('./chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the provided URL
    driver.get("https://nedm.ytmnd.com/")

    # Wait for 12 seconds
    time.sleep(12)

    # Get the dimensions of the window
    window_size = driver.get_window_size()
    center_x = window_size['width'] // 2
    center_y = window_size['height'] // 2

    # Simulate a click at the center of the screen
    actions = ActionChains(driver)
    actions.move_by_offset(center_x, center_y).click().perform()

    # Wait for 10 seconds
    time.sleep(10)

finally:
    # Close the browser
    driver.quit()