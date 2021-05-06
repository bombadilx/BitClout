def login(driver,time):
    # Asking the user for their private phrase to login to the account
    a = 0

    while a == 0:

        PRIVATE_PHRASE = input("your phrase")

        # Fetching BITCLOUT.COM
        driver.get("https://bitclout.com/")

        # Defining the login button and clicking it
        time.sleep(2)
        login_button = driver.find_element_by_xpath('/html/body/app-root/div/app-landing-page/div[2]/div/div/div['
                                                    '2]/a[2]')
        login_button.click()

        another_window = list(set(driver.window_handles) - {driver.current_window_handle})[0]
        driver.switch_to.window(another_window)

        # Loading the account with PRIVATE PHRASE
        load_account_textbox = driver.find_element_by_class_name('form-control')

        # the thing to do is to enter the phrase here instead of "PRIVATE_PHRASE"
        load_account_textbox.send_keys(str(PRIVATE_PHRASE))
        login_button = driver.find_element_by_xpath('/html/body/app-root/div/app-log-in/div/div/div[4]/button')
        login_button.click()

        # Clicks the load account button
        load_account_button = driver.find_element_by_css_selector('button')
        load_account_button.click()
        time.sleep(2)
        current_window = driver.window_handles
        driver.switch_to.window(current_window[0])
        time.sleep(2)

        print(driver.current_url)

        if driver.current_url != 'https://bitclout.com/log-in':
            print("░ You are now logged in...")
            break
        else:
            print("░ There was an error logging into your account... Please check your private phrase and try again...")
