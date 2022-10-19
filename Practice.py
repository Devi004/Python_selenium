from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Users\dpp69\Desktop\Python\chromedriver.exe")
driver.get("http://primusbank.qedgetech.com/")

driver.find_element_by_name("txtuId").send_keys("Admin")
driver.find_element_by_name("txtPword").send_keys("Admin")
driver.find_element_by_name("login").click()

exp_title="Primus Bank"
act_title=driver.title

if(exp_title==act_title):

    print("Test case passed")

else:

    print("Test cases passed")


driver.close





