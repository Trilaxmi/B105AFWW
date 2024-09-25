from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Chrome
class LoginPage:
    def __init__(self, driver):
        self.driver=driver
        self.__un=(By.NAME,"username")
        self.__pw=(By.NAME,"password")
        self.__go=(By.NAME,"login-button")
        self.__errmsg=(By.XPATH,"//div[text()='Invalid username and/or password.']")

    def set_un(self,un):
        self.driver.find_element(*self.__un).send_keys(un)

    def set_pw(self,pw):
        self.driver.find_element(*self.__pw).send_keys(pw)

    def click_go(self):
        self.driver.find_element(*self.__go).click()

    def verify_errmsg_is_displayed(self,wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__errmsg))
            print("error displayed")
            return True
        except:
            print("error not displayed")
            return False

