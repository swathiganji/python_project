from selenium import webdriver
import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...","..."))
from SampleProjects.POMProjectDemo.Pages.loginPage import Loginpage
from SampleProjects.POMProjectDemo.Pages.homePage import Homepage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/sree8/PycharmProjects/pythonProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        loginPage = Loginpage(driver)
        loginPage.enter_username("Admin")
        loginPage.enter_password("admin123")
        loginPage.click_login()

        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()




        #self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_id("btnLogin").click()
        #self.driver.find_element_by_id("welcome").click()
        #self.driver.find_element_by_link_text("Logout").click()
        time.sleep(3)
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sree8/PycharmProjects/pythonProject/Reports'))

