from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\dpp69\\Desktop\\Python\\chromedriver.exe")
driver.get("https://www.google.com/")

driver.find_element(By.NAME,"q").send_keys("Selenium Openings")

alloptions=driver.find_elements(By.CSS_SELECTOR,"ul.erkvQe li span")

for i in alloptions:

    if (i.text) == "selenium openings in pune":

        driver.implicitly_wait(20)

        i.click()
        break
    


driver.close()
