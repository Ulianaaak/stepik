import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys(y)
print(x)
print(y)
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = browser.find_element(By.ID, "peopleRule")
option2.click()
option3 = browser.find_element(By.ID, "robotsRule")
option3.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()