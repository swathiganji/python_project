import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()
path ="C:/selenium/DataDriven.xlsx"
rows = XLUtils.getRowCount(path,'sheet1')
for r in range(2,rows+1):
    username=XLUtils.readData(path,'sheet1',r,1)
    password=XLUtils.readData(path,'sheet1',r,2)

    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    if 