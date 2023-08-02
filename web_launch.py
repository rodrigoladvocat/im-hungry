from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
from selenium.webdriver.support.wait import WebDriverWait
from log_gmail import pull_code
from dotenv import load_dotenv, find_dotenv
import os

def launch_ifood(order) -> None:
    load_dotenv(find_dotenv())

    service = EdgeService('msedgedriver.exe')
    driver = webdriver.Edge(service=service)

    driver.get('https://ifood.com.br/entrar/email')

    element = driver.find_element(By.CLASS_NAME, 'simple-form-input__field')
    element.send_keys(os.getenv('email'))
    element.submit()

    time.sleep(8)

    ifood_code = pull_code()

    for i in range(6):
        code_div = driver.find_element(By.ID, f'otp-input-{i}')
        code_div.send_keys(ifood_code[i])
        code_div.submit()

    time.sleep(5)

    home_addr = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/button[1]')
    home_addr.click()

    time.sleep(3)

    driver.quit()
    return
