from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

# navigation to BitClout.com
driver.get("https://bitclout.com/")

# Asking the user for their private phrase to login to the account
PRIVATE_PHRASE = input("░ What is your BitClout private phrase?: ")

# Defining the login button and clicking it
login_button = driver.find_element_by_xpath('/html/body/app-root/div/app-landing-page/div[2]/div/div/div[2]/a[2]')
login_button.click()

# Loading the account with PRIVATE PHRASE
load_account_textbox = driver.find_element_by_css_selector('textarea')
load_account_textbox.send_keys(str(PRIVATE_PHRASE))

# Clicks the load account button
load_account_button = driver.find_element_by_css_selector('button')
load_account_button.click()

print(driver.current_url)
driver.close()
