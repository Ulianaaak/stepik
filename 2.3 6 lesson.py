from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
but = browser.find_element(By.ID, "book")
but.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
inp2 = browser.find_element(By.ID, "answer")
inp2.send_keys(y)

button_end = browser.find_element(By.ID, "solve")
button_end.click()

time.sleep(20)
# закрываем браузер после всех манипуляций
browser.quit()