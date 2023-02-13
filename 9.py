from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    
    x1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x1.text)
    y1 = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y1.text)


    
    z = x+y
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z)) # ищем элемент с текстом "Python"



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()