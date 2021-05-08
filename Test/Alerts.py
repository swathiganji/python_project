from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
#driver.switch_to_alert().accept()#closing the alert window by clicking ok button
driver.switch_to_alert().dismiss()#closing alert by clicking cancle button
