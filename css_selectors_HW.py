from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#navigate to Sign In page
driver.find_element(By.ID, 'nav-link-accountList').click()

#navigate to Create Account page
driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()

#Amazon Logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#Create Account image
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Name Field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Mobile Number or Email Field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#Password Field
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#Password Requirement
driver.find_element(By.XPATH, ("//div[contains(text(), 'Passwords must be')]"))

#Re-enter Password Field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Continue Button
driver.find_element(By.CSS_SELECTOR, '#continue')

#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_register_notification_condition_of_use?']")

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_register_notification_privacy_notice?']")

#Sign in link
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?']")

driver.quit()

