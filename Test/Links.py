from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.kayak.com/")
links=driver.find_elements_by_tag_name("a")
print("number of links present:",len(links))
for link in links:
    print(link.text)#how many links present in a page
#clicking on link
driver.find_element_by_link_text("Flights").click()