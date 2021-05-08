from selenium import webdriver

from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.implicitly_wait(10)
#assert "Volunteer Sign Up" in driver.title
#print(driver.title)
#x= driver.title
#assert x == "Volunteer Sign Up"
#How to find how many input boxes are present in the web page
inputboxes = driver.find_elements_by_class_name("text_field")
print(len(inputboxes))

first_name=driver.find_element_by_id("RESULT_TextField-1")
print(first_name.is_selected())
print(first_name.is_enabled())
first_name.send_keys("John")
last_name=driver.find_element_by_id("RESULT_TextField-2")
print(last_name.is_selected())
print(last_name.is_enabled())
last_name.send_keys("Smith")
driver.find_element_by_id("RESULT_TextField-3").send_keys("33333333333")
driver.find_element_by_id("RESULT_TextField-4").send_keys("US")
driver.find_element_by_id("RESULT_TextField-5").send_keys("Tampa")
driver.find_element_by_id("RESULT_TextField-6").send_keys("swathi@gmail.com")
#working with radiobuttons
status = driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(status)#true or false

driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[2]/td/label").click()
#working with checkboxes
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[4]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[6]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()
#working with dropdown
element = driver.find_element_by_class_name("drop_down")
drp = Select(element)
#select by visible_text
drp.select_by_visible_text("Morning")
#select by value
#drp.select_by_value("Radio-2")
#select by index
#drp.select_by_index(3)

