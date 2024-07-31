import pytest
from PageObjects.UserprofilePage import User_profile
from Utilities.Logger import Logging_Class


@pytest.mark.regression
class Test_login_param:

    log = Logging_Class.log_generator()

    def test_login003(self,setup,getDataForLogin):
        self.log.info("Test case start")
        self.log.info("opening browser")
        self.driver = setup
        self.ur = User_profile(self.driver)
        self.log.info("click on logi link")
        self.ur.click_login_link()
        self.log.info("Enter Email id")
        self.ur.enter_email(getDataForLogin[0])
        self.log.info("Enter password")
        self.ur.enter_password(getDataForLogin[1])
        self.log.info("click on login button")
        self.ur.click_login_button()
        self.log.info("check login pass or fail")
        validation = self.ur.validate_login()

        if validation == "pass" and getDataForLogin[2] == "pass":
            self.log.info("login successful, TC pass")
            print(validation)
            self.driver.save_screenshot(".\\Screenshots\\login_pass_TC_pass.PNG")
            assert True

        elif validation == "pass" and getDataForLogin[2] == "fail":
            self.log.info("TC fail")
            print(validation)
            self.driver.save_screenshot(".\\Screenshots\\login_pass_TC_fail.PNG")
            assert False

        elif validation == "fail" and getDataForLogin[2] == "fail":
            self.log.info("TC pass")
            print(validation)
            self.driver.save_screenshot(".\\Screenshots\\login_fail_TC_pass.png")
            assert True

        elif validation == "fail" and getDataForLogin[2] == "pass":
            self.log.info("TC fail")
            print(validation)
            self.driver.save_screenshot(".\\Screenshots\\login_fail_TC_fail.PNG")
            assert False



