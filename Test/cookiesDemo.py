from selenium import webdriver

driver=webdriver.Chrome("C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
driver.get("https://www.amazon.com/")
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#add cookies
cookie={'name':'mycookie','value':'977656778'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
#delete cookie
driver.delete_cookie('mycookie')
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
#deleting all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)