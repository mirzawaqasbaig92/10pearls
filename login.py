
from lib import *
from variable import *

def logIn(user, password):
    global driver
    driver.maximize_window()
    driver.get(url)
    #driver.implicitly_wait(3)
    driver.find_element(By.ID,"user-name").send_keys(user) 
    driver.find_element(By.ID,"password").send_keys(password + Keys.ENTER)
    driver.implicitly_wait(3)
    print(driver.current_url)
    if driver.current_url == url_success: 
        print("Pass")
    else :
        print("Fail")
    driver.implicitly_wait(1)


for entry in users:
    logIn(entry, password)