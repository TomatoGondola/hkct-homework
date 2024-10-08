from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://hk.on.cc/hk/bkn/cnt/news/20240928/bkn-20240928162253149-0928_00822_001.html"
driver.get(url)
search = driver.find_element(by=By.CSS_SELECTOR, value="div[class='videoCube trc_spotlight_item origin-default textItem thumbnail_start videoCube_5_child'] a:nth-child(2) span:nth-child(1) span:nth-child(1)").text
para = driver.find_element(By.XPATH, value="//div[contains(@class,'paragraph') and contains(text(), ''").text
print(search, para)

# search.send_keys("Persian Cat")
time.sleep(3)
driver.close()
# driver.findElement(By.cssSelector("))
# driver.findElement(By.xpath("//div[contains(@class,'paragraph')][contains(text(),'醫院管理局指兩名參與該縫合手術程序的員工今晨被捕，她們將被暫停職務。醫院將遵循現行的人力資源政策處理')]"))