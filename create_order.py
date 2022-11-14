import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
input_mail.send_keys('XXXXXXxxxx@XXX')
next_step=driver.find_element(By.XPATH,'/html/body/div/div[4]/form/div[2]/div[3]/div/button/span[3]')
next_step.click()
psswd=driver.find_element(By.NAME,'password')
psswd.send_keys('***************')
login_button=driver.find_element(By.ID,'loginButton')
login_button.click()

search= driver.find_element(By.ID,'fi-q')
search.send_keys("cable iphone")
rechercher=driver.find_element(By.XPATH,'//*[@id="search"]/button')
rechercher.click()



find_locator=driver.find_element(By.XPATH,'//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[1]/a/div[1]/img')
find_locator.click()
product=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[1]/footer/form/button')))
product.click()


buy_product=driver.find_element(By.XPATH,'//*[@id="add-to-cart"]/button/span')
buy_product.click()
time.sleep(6)

driver.find_element(By.XPATH,'//*[@id="add-to-cart"]/button[2]').click()
time.sleep(3)
cart=driver.find_element(By.XPATH,'//*[@id="jm"]/header/section/div[2]/a')
cart.click()
commander=driver.find_element(By.XPATH,'//*[@id="jm"]/main/div/div[2]/div/article/div[2]/a')
commander.click()

next_etape=driver.find_element(By.XPATH,'//*[@id="osh-opc-btn-save"]')
next_etape.click()
payment_mode=driver.find_element(By.XPATH,'//*[@id="osh-opc-paymentForm"]/div[3]/div[2]/label')
payment_mode.click()
code_promo=driver.find_element(By.XPATH,'//*[@id="opc-cart-promocode"]')
code_promo.send_keys('k-samibf')
time.sleep(3)
ajouter_coupon=driver.find_element(By.XPATH,'//*[@id="osh-opc-paymentForm"]/div[4]/div[2]/button/span')
ajouter_coupon.click()

confirm_order=driver.find_element(By.XPATH,'//*[@id="osh-opc-paymentForm"]/button').click() 
detail_order=driver.find_element(By.XPATH,'//*[@id="jm"]/main/div/div[1]/div/div[1]/article/a').click()
suivez_colis=driver.find_element(By.XPATH,'//*[@id="jm"]/main/div/section/div/div/section[2]/article/div/div[2]/a').click()






