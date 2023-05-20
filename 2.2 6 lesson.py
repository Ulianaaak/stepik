import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

option1 = browser.find_element(By.CLASS_NAME, "form-check-input")
option1.click()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
option3 = browser.find_element(By.ID, "robotsRule")
option3.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
