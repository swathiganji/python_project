from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button")
print(driver.current_window_handle)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

driver.quit()