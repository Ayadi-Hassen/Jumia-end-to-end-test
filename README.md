# Jumia-end-to-end-test
The creation and cancellation of an order with Selenium

## Installation
git clone https://github.com/Ayadi-Hassen/Jumia-end-to-end-test

cd Jumia-end-to-end-test

## Requirements
We have used Chromedriver for automated testing


```python
# Install Chromedriver
PATH =  "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

```



## Usage
```python
# sign in
sign_in=driver.find_element(By.XPATH,'/html/body/div/div[4]/form/div[2]/div[2]/label/input')
sign_in.send_keys('input your user_name')
psswd=driver.find_element(By.NAME,'password')
psswd.send_keys('input your password')
login_button=driver.find_element(By.ID,'loginButton').click()

```
- sign_in : Jumia account username.
- passwd :  Jumia account password.

This will allow access to your jumia account. 

## Search Product 
This will allow to find product 

```python
search= driver.find_element(By.ID,'fi-q').send_keys("cable iphone")
rechercher=driver.find_element(By.XPATH,'//*[@id="search"]/button').click()

```
## Create Order 

This will allow to buy product. We have used different ways for example: By.ID, By.XPATH, By.NAME... 

```python

buy_product=driver.find_element(By.XPATH,'//*[@id="add-to-cart"]/button/span').click()

```

## Cancel Order 
This will allow how to cancel the order. We have used the SELECT method for example : select_by_index, select_by_value.

```python

your_orders=driver.find_element(By.XPATH,'//*[@id="dpdw-login-box"]/div/a[2]').click()
cancel_order_button=driver.find_element(By.XPATH,'//*[@id="jm"]/main/div/section/div/div/section[2]/article/div/div[2]/form/button').click()


```
## Want to help 
If you like this application, please star this repository.

If you create an app using this application, please mention this repository.

If you want to contribute to this application, feel free to create a pull request

## Contact 

[LinkedIn](https://www.linkedin.com/in/hassen-ayadi-8534661ba/)
