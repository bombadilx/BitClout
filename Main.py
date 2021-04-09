import os

from Login import *
from AutoLike import *
from AutoComment import *
from AutoReclout import *
from AutoBUY import *
from AutoSELL import *
from UNDERVALUED_USER_ALERT import *

directory = os.path.dirname(__file__)
chrome_driver_path = directory + "\chromedriver.exe"

driver = driver.Chrome(chrome_driver_path)

"""-------------

Global bot settings go here

-------------"""

login()

while True:
    # TODO: Run like function
    like()
    # TODO: Run comment function
    comment()
    # TODO: Run reclout function
    reclout()
    # TODO: Run buy function
    buy()
    # TODO: Run sell function
    sell()
    # TODO: Run UNDERVALUED_USER_ALERT
    alert()
