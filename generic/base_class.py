import os
import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pyjavaproperties import Properties
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

class BaseClass:

    @pytest.fixture(autouse=True)
    def pre_condition(self):

        generic=os.path.dirname(__file__)
        print('path of generic file:', generic)
        self.XLPATH=generic+"/../data/input.xlsx"
        ppt_obj=Properties()
        ppt_obj.load(open(generic+"/../config.properties"))
        grid=ppt_obj['GRID']
        grid_url=ppt_obj['GRID_URL']
        browser=ppt_obj['BROWSER']
        app_url=ppt_obj['APP_URL']
        ito=ppt_obj['ITO']
        eto=ppt_obj['ETO']

        if grid.lower()=='no':
            print("\n open chrome browser in local:",browser)
            if browser.lower()=='chrome':
                self.driver=Chrome()
            else:
                self.driver=Firefox()
        else:
            print("\n open chrome browser in Remote:",browser)
            if browser.lower()=='Chrome':
                chrome_options= ChromeOptions()
                chrome_options = Options
                self.driver=webdriver.Remote(command_executor=grid_url, options=chrome_options)
            else:
                firefox_options=FirefoxOptions()
                self.driver=webdriver.Remote(command_executor=grid_url, options=firefox_options())

        print("enter the url",app_url)
        self.driver.get(app_url)

        print("set ITO", ito)
        self.driver.implicitly_wait(ito)

        print("set ETO",eto)
        self.wait=WebDriverWait(self.driver,eto)

        print("maximize the browser")
        self.driver.maximize_window()
        time.sleep(3)

    @pytest.fixture(autouse=True)
    def post_condition(self):
        yield
        print("close the browser")
        self.driver.quit()


