from selenium import webdriver
from POMDemoProject.Pages.LoginPage import LoginPage
from POMDemoProject.Pages.HomePage import HomePage

import time
import unittest



# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/home/info/PycharmProjects/SampleSeleniumProject/browsers/chromedriver")

        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()


    def test_login_valid(self):
        driver = self.driver

        login = LoginPage(driver)
        homepage = HomePage(driver)

        login.enter_username("Admin31")
        login.enter_password("admin123")
        login.click_loginBtn()

        homepage.click_welcome_link()
        homepage.click_logout_link()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.implicitly_wait(2)
        # self.driver.find_element_by_link_text("Logout").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")

    # if __name__ == "__main__":
    #     unittest.main(HTMLTestRunner.HTML)


