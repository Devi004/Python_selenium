# from select import select
#from select import select
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

driver.maximize_window

driver.get("https://www.facebook.com/")

driver.implicitly_wait(20)

driver.find_element(By.XPATH,"(//a[normalize-space()='Create New Account'])[1]").click()
driver.find_element(By.NAME,"firstname").send_keys("Devi Prasad")
driver.find_element(By.NAME,"lastname").send_keys("Pattanayak")
driver.find_element(By.NAME,"reg_email__").send_keys("9437737233")
driver.find_element(By.NAME,"reg_passwd__").send_keys("Dpp69699@")

x = driver.find_element(By.XPATH,"//select[@id='day']")
Drop_day = Select(x)
Drop_day.select_by_value(("5"))

x1 = driver.find_element(By.XPATH,"//select[@id='month']")
Drop_month = Select(x1)
Drop_month.select_by_visible_text("Mar")
x3 = driver.find_element(By.XPATH,"//select[@id='year']")
Drop_year = Select(x3) 
Drop_year.select_by_value("2018")

allop=Drop_year.options
for i in allop:
    print(i)

driver.find_element(By.XPATH,"//label[contains(text(),'Male')]").click()
driver.find_element(By.XPATH,"//button[@id='u_0_s_xG']").click()




















