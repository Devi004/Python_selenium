from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time

browser="chrome"

if (browser=="chrome"):

    driver = webdriver.Chrome(ChromeDriverManager().install())

elif(browser=="firefox"):

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

else:

    print("Enter correct browser")

driver.get("https://www.yatra.com/")
print(driver.current_url)
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"(//img[@alt='Flat 16% OFF (upto Rs.2,022)'])[1]").click()
driver.find_element(By.XPATH,"(//img[@alt='Flat 16% OFF (upto Rs.2,022)'])[2]").click()
driver.find_element(By.XPATH,"(//img[@alt='Flat 16% OFF (upto Rs.2,022)'])[3]").click()


child_window=driver.window_handles

driver.switch_to.window(child_window[2])
driver.close()
time.sleep(5)
driver.switch_to.window(child_window[0])
time.sleep(10)
driver.close()