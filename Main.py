import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Login import login
from AutoLike import *
from AutoComment import *
from AutoReclout import *
from AutoBUY import *
from AutoSELL import *
from UNDERVALUED_USER_ALERT import *

"""----------------------------------------"""

# GLOBAL BITCLOUT BOT SETTINGS
AutoLike = 'on'
AutoComment = 'OFF'
AutoReclout = 'on'
AutoBUY = 'on'
AutoSELL = 'on'
UNDERVALUED_USER_ALERT = 'on'

"""----------------------------------------"""

driver = webdriver.Chrome(ChromeDriverManager().install())
os.system('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')

print('░ WELCOME TO BITCLOUT BOT!')

EMAIL_ADDITION = input("░ What is your email address for alerts from BITCLOUT BOT?: ")

time.sleep(1)

login(driver, time)

if AutoLike == 'on':
    # TODO: Run like function
    like(driver)
else:
    print("░ AutoLike IS NOT ON.. SKIPPING...")
    pass

if AutoComment == 'on':
    # TODO: Run comment function
    comment(driver)
else:
    print("░ AutoComment IS NOT ON.. SKIPPING...")
    pass

if AutoReclout == 'on':
    # TODO: Run reclout function
    reclout(driver)
else:
    print("░ AutoReclout IS NOT ON.. SKIPPING...")
    pass

if AutoBUY == 'on':
    # TODO: Run buy function
    buy(driver)
else:
    print("░ AutoBUY IS NOT ON.. SKIPPING...")
    pass

if AutoSELL == 'on':
    # TODO: Run sell function
    sell(driver)
else:
    print("░ AutoSELL IS NOT ON.. SKIPPING...")
    pass

if UNDERVALUED_USER_ALERT == 'on':
    # TODO: Run UNDERVALUED_USER_ALERT
    alert(driver)
else:
    print("░ UNDERVALUED_USER_ALERT IS NOT ON.. SKIPPING...")
    pass

print("░ PROGRAM IS NO LONGER RUNNING")
