from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Specify the path to the geckodriver executable
service_obj = Service('./geckodriver')  # Ensure this path is correct

# Specify the path to the Firefox binary
firefox_options = Options()
firefox_options.binary_location = '/usr/bin/firefox-bin'  # Update this path to your Firefox binary location

# Initialize the Firefox driver with the service object and options
driver = webdriver.Firefox(service=service_obj, options=firefox_options)

# Define the URL to navigate to
url = "https://www.gentoo.org"

# Open the URL in the browser
driver.get(url)

# Wait for 3 seconds
time.sleep(3)

# Close the browser
driver.close()