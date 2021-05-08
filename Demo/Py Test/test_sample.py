from selenium import webdriver
import pytest
class TestSample():
    @ pytest.fixture()
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome("C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self,test_setUp):
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x = driver.title
        assert x == "OrangeHRM"
    #def test_tearDown():
     #  driver.close()
      # driver.quit()
    #  print("Test completed")