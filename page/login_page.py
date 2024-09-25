from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Chrome
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.__un=(By.NAME,"username")
        self.__pw=(By.NAME,"password")
        self.__go=(By.NAME, "login_button")

    def set_un(self,un):
        self.driver.findelement(*self.__un).sendkeys(un)

    def set_pw(self,pw):
        self.driver.findelement(*self.__pw).sendkeys(pw)

    def click_go(self):
        self.driver.findelement(*self.__go).click()


