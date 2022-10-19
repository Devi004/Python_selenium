from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browser="chrome"

if (browser=="chrome"):

    driver = webdriver.Chrome(ChromeDriverManager().install())

elif(browser=="firefox"):

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

else:

    print("Enter correct browser")
driver.maximize_window
driver.get("http://orangehrm.qedgetech.com/")
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("Qedge123!@#")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
driver.implicitly_wait(30)
print(driver.title)