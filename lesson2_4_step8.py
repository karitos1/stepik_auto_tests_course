from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = browser.find_element(By.ID, "price").text

# говорим Selenium проверять в течение 12 секунд, пока цена не опустится до $100
need_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
book = browser.find_element(By.ID, "book")
book.click()

x = browser.find_element(By.ID, "input_value").text
inp = browser.find_element(By.ID, "answer")
inp.send_keys(str(math.log(abs(12*math.sin(int(x))))))
submit = browser.find_element(By.ID, "solve")
submit.click()
