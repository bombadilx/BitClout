import os

from Login import login
from AutoLike import like
from AutoComment import comment
from AutoReclout import reclout
from AutoBUY import buy
from AutoSELL import sell
from UNDERVALUED_USER_ALERT import alert

dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

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
