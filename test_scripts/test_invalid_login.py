from generic.base_class import BaseClass
from page.login_page import LoginPage
from page.home_page import HomePage
from generic.utility import Excel
class Test_InvalidLogin(BaseClass):
    # read data
    def test_invalid_login(self):

        un=Excel.get_data(self.XLPATH, 'InvalidLogin', 2,1)
        pw=Excel.get_data(self.XLPATH, 'InvalidLogin', 2,2)


        # Enter valid username
        login_page=LoginPage(self.driver)
        login_page.set_un(un)

        # Enter valid password
        login_page.set_pw(pw)

        # Click on go button
        login_page.click_go()

        # Verify homepage is displayed.
        result=login_page.verify_errmsg_is_displayed(self.wait)
        assert result



