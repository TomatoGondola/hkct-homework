from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://hk.on.cc/hk/bkn/cnt/news/20240928/bkn-20240928162253149-0928_00822_001.html"
driver.get(url)

# Corrected CSS selector
search = driver.find_element(By.CSS_SELECTOR, "div[class='videoCube trc_spotlight_item origin-default textItem thumbnail_start videoCube_5_child'] a:nth-child(2) span:nth-child(1) span:nth-child(1)").text

# Corrected XPath for the paragraph element
para = driver.find_element(By.XPATH, "//div[contains(@class, 'paragraph') and contains(text(), '醫院管理局指兩名參與該縫合手術程序的員工今晨被捕，她們將被暫停職務。醫院將遵循現行的人力資源政策處理')]").text

print(para)

time.sleep(3)
driver.close()