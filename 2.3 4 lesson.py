from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
inp = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
inp.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
inp2 = browser.find_element(By.ID, "answer")
inp2.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()