from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math,os

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла