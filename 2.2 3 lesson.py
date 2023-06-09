from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


n1 = browser.find_element(By.ID, "num1")
n2 = browser.find_element(By.ID,"num2")

x = n1.text
y = n2.text
s = int(x) + int(y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(s))


button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()

time.sleep(30)
browser.quit()