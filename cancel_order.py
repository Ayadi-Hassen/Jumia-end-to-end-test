import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import random
import string
import time
PATH =  "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
wait=WebDriverWait(driver,30)

jumia_home_page= 'https://www.jumia.com.tn/'
driver.get(jumia_home_page)
driver.implicitly_wait(3)
driver.maximize_window()


def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))


email=random_char(7)+"@gmail.com"
print(email)

quitter=driver.find_element(By.XPATH,'//*[@id="fi-nl-pop-email"]')
quitter.send_keys(email)
gender=driver.find_element(By.XPATH,'//*[@id="nl-pop-f"]/div[2]/button[1]')
gender.click()

connect=driver.find_element(By.XPATH,'//*[@id="jm"]/header/section/div[2]/div[1]/label')
connect.click()
my_account=driver.find_element(By.XPATH,'//*[@id="dpdw-login-box"]/div/a[1]')
my_account.click()
input_mail=driver.find_element(By.XPATH,'/html/body/div/div[4]/form/div[2]/div[2]/label/input')
input_mail.send_keys('XXXXXXXX@XXX.xxx')
next_step=driver.find_element(By.XPATH,'/html/body/div/div[4]/form/div[2]/div[3]/div/button/span[3]')
next_step.click()
psswd=driver.find_element(By.NAME,'password')
psswd.send_keys('************')
login_button=driver.find_element(By.ID,'loginButton')
login_button.click()

connect=driver.find_element(By.XPATH,'//*[@id="jm"]/header/section/div[2]/div[1]/label')
connect.click()


vos_commande=driver.find_element(By.XPATH,'//*[@id="dpdw-login-box"]/div/a[2]').click()

driver.find_element(By.XPATH,'//*[@id="jm"]/main/div/section/div/div/div[2]/article/div/a').click()
if not driver.find_elements(By.XPATH,'//*[@id="jm"]/main/div/section/div/div/section[2]/article/div/div[2]/form/button') :
    print("You can't Cancel the order now please wait until provider accepts the order ")
else:
    cancel_order_button=driver.find_element(By.XPATH,'//*[@id="jm"]/main/div/section/div/div/section[2]/article/div/div[2]/form/button')
    cancel_order_button.click()
    quantity=driver.find_element(By.ID,'fi-quantity')

    select_quantity=Select(quantity)
    select_quantity.select_by_index(len(select_quantity.options) - 1)

    reason=driver.find_element(By.ID,'fi-reason')
    select_reason=Select(reason)
    select_reason.select_by_value("486")
    driver.find_element(By.XPATH,'//*[@id="askCancel"]/div[3]/button').click()