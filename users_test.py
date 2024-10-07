from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import time
import os

load_dotenv()

url = 'http://users.bugred.ru/'
browser = webdriver.Chrome()
login_manager = 'manager@mail.ru'
password_manager = '1'
log_mail_pass_text = ['new_user_1000', 'new_mail_1000@mail.ru', '111']
avatar_file = os.getenv('PHOTO_PATH')
other_info_text = ['name1', 'surname1', 'patronymic1', 'мася', 'бобик', 'кеша', 'проскофья', 'булочка', 'орешек', '88005353535', 'Ул. Проспект Вернадского д. 64', '7743013902']

try:
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(10)

    enter = browser.find_element(By.XPATH, '(//li[@class="newlink"])[2]')
    enter.click()

    loging_m = browser.find_element(By.NAME, 'login')
    loging_m.send_keys(login_manager)

    password_m = browser.find_element(By.NAME, 'password')
    password_m.send_keys(password_manager)

    log_in = browser.find_element(By.XPATH, '//input[@class="btn btn-danger"]')
    log_in.click()

    create_new_user = browser.find_element(By.XPATH, '//a[@class="btn btn-danger"]')
    create_new_user.click()

    name_mail_password = browser.find_elements(By.XPATH, '(//table//tr)[position() <= 3]//td[position() mod 2 = 0]//input')

    for i in range(len(name_mail_password)):
        if i < len(log_mail_pass_text):
            name_mail_password[i].send_keys(log_mail_pass_text[i])

    avatar = browser.find_element(By.XPATH, '//table//tr[4]/td[2]//input')
    avatar.send_keys(avatar_file)

    born_date = browser.find_element(By.XPATH, '//table//tr[5]/td[2]//input')
    born_date.send_keys('10-05-2000')

    gender_input = browser.find_element(By.XPATH, '//table//tr[6]/td[2]//select')
    select_input = Select(gender_input)
    select_input.select_by_index(2)

    start_work = browser.find_element(By.XPATH,'//table//tr[7]/td[2]//input')
    start_work.send_keys('23-10-2020')

    hobby = browser.find_element(By.XPATH, '//table//tr[8]/td[2]//textarea')
    hobby.send_keys('Прыгаю со скакалкой')

    other_info = browser.find_elements(By.XPATH, '(//table//tr)[position() >= 9 and position() < last()]//td[position() mod 2 = 0]//input[not(contains(@style, "display:none"))]')
    for i in range(len(other_info)):
        if i < len(other_info_text):
            other_info[i].send_keys(other_info_text[i])

    # time.sleep(5)
    act_create = browser.find_element(By.NAME, 'act_create')
    act_create.click()

finally:
    time.sleep(300)
    browser.quit()
