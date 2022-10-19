from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import time

browser="chrome"

if (browser=="chrome"):

    driver = webdriver.Chrome(ChromeDriverManager().install())

elif(browser=="firefox"):

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

else:

    print("Enter correct browser")

driver.get("https://www.yatra.com/")
driver.implicitly_wait(20)
driver.maximize_window

depart_from=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
depart_from.click()
time.sleep(5)
depart_from.send_keys("Bangalore")
time.sleep(5)
depart_from.send_keys(Keys.ENTER)
time.sleep(5)
depart_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
depart_to.click()
time.sleep(5)
depart_to.send_keys("Mumbai")
time.sleep(5)





#wait=WebDriverWait(driver,10)

#wait.until(EC.element_to_be_clickable(By.XPATH,"//input[@id='BE_flight_origin_date']")).click()
#all_dates=driver.find_elements(By.XPATH,"//input[@id='BE_flight_origin_date']")

#for dates in all_dates:

   # if dates.get_attribute("date-date")=="30/10/2022":

        #dates.click()
        #break
#driver.find_element(By.XPATH,"(//input[@id='BE_flight_flsearch_btn'])[1]")
#time.sleep(20)



