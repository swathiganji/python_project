from SampleProjects.POMProjectDemo.Locators.locators import Locators
class Loginpage():
    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = "txtPassword"
        self.login_button_id     = "btnLogin"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys("Admin")
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys("admin123")
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
