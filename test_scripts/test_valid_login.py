from generic.base_class import BaseClass
from page.login_page import LoginPage
from page.home_page import HomePage
from generic.utility import Excel
class Test_ValidLogin(BaseClass):
    # read data
    def test_validlogin(self):

        un=Excel.get_data(self.XLPATH, 'ValidLogin', 2,1)
        pw=Excel.get_data(self.XLPATH, 'ValidLogin', 2,2)


    # Enter valid username
        login_page=LoginPage(self.driver)
        login_page.set_un(un)

    # Enter valid password
        login_page.set_pw(pw)
    # Click on go button
        login_page.click_go()
    # Verify homepage is displayed.
        home_page=HomePage(self.driver)
        result=home_page.verify_homepage_is_displayed(self.wait)
        assert result



