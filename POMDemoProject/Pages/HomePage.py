class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_bt_text = "Logout"

    def click_welcome_link(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
        self.driver.implicitly_wait(2)

    def click_logout_link(self):
        self.driver.find_element_by_link_text(self.logout_link_bt_text).click()
        self.driver.implicitly_wait(2)


