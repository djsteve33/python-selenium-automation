from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#navigate to Sign In page
driver.find_element(By.ID, 'nav-link-accountList').click()

#Amazon Logo
driver.find_element(By.XPATH, "//*[@aria-label='Amazon']")

#Email field
driver.find_element(By.ID, "ap_email")

#Continue button
driver.find_element(By.ID, "continue")

#Need help link
driver.find_element(By.XPATH, "//*[contains(text(), 'help')]").click()

#Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

#Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

#Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

#Conditions of use link
driver.find_element(By.XPATH,"//a[contains(@href, 'condition_of_use')]")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'privacy_notice')]")

driver.quit()

##############################################################
# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Click Orders
driver.find_element(By.ID, "nav-orders").click()

#Sign In header is visible
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in')]").text
print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')

#email input field is present
expected_result_2 = 'email'
actual_result_2 = driver.find_element(By.XPATH, "//input[@type='email']").text
print(actual_result_2)

assert expected_result_2 == actual_result_2, f'Expected {expected_result_2} but got actual {actual_result_2}'
print('Test case #2 passed')

driver.quit()