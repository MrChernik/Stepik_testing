from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html" #28.938472438980682
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")

    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    

    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))
