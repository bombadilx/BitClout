def login(driver,time):
    # Asking the user for their private phrase to login to the account
    a = 0

    while a == 0:

        PRIVATE_PHRASE = input("░ What is your BitClout private phrase? (WE DO NOT SAVE THIS): ")

        # Fetching BITCLOUT.COM
        driver.get("https://bitclout.com/")

        # Defining the login button and clicking it
        time.sleep(2)
        login_button = driver.find_element_by_xpath('/html/body/app-root/div/app-landing-page/div[2]/div/div/div['
                                                    '2]/a[2]')
        login_button.click()

        # Loading the account with PRIVATE PHRASE
        load_account_textbox = driver.find_element_by_css_selector('textarea')
        load_account_textbox.send_keys(str(PRIVATE_PHRASE))

        # Clicks the load account button
        load_account_button = driver.find_element_by_css_selector('button')
        load_account_button.click()

        time.sleep(2)

        print(driver.current_url)

        if driver.current_url != 'https://bitclout.com/log-in':
            print("░ You are now logged in...")
            break
        else:
            print("░ There was an error logging into your account... Please check your private phrase and try again...")