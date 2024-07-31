import pytest

from PageObjects.LoginPage import Login_Class
from Utilities.Logger import Logging_Class
from Utilities import XLUTILIES


class Test_DDT:

    log = Logging_Class.log_generator()
    path = ".\\TestData\\LoginData.xlsx"

    @pytest.mark.ddt2
    def test_DDT_002(self, setup):
        self.log.info("Testcase test_CredKart_url_DDT_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("Click On login Link")
        self.lg.Login_Link()
        self.rows = XLUTILIES.rows_count(self.path,'sheet1')
        Result_List = []
# 5
        for r in range(2, self.rows+1):
            self.Email = XLUTILIES.read_data(self.path,'sheet1', r,1)
            self.Password = XLUTILIES.read_data(self.path, 'sheet1', r, 2)
            self.exp_result = XLUTILIES.read_data(self.path, 'sheet1', r, 3)

            self.log.info("Enter Email")
            self.lg.Enter_Email(self.Email)
            self.log.info("Enter Password")
            self.lg.Enter_Password(self.Password)
            self.log.info("Click Login Button")
            self.lg.Click_Login_Button()
            self.log.info("Verify Login Stauts")

            if  self.exp_result == "Login_Pass" and self.lg.Verify_Login_Status() == "Pass":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
                XLUTILIES.read_write(self.path, 'sheet1', r, 4, "Login_Pass")
                Result_List.append("Pass")
                self.lg.Click_Menu_Button()
                self.lg.Click_Logout_Button()
                self.lg.Login_Link()

            elif self.exp_result == "Login_Pass" and self.lg.Verify_Login_Status() == "Fail":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
                XLUTILIES.read_write(self.path, 'sheet1', r, 4, "Login_Fail")
                Result_List.append("Fail")
                self.lg.Login_Link()

            elif self.exp_result == "Login_Fail" and self.lg.Verify_Login_Status() == "Pass":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
                XLUTILIES.read_write(self.path, 'sheet1', r, 4, "Login_Fail")
                Result_List.append("Fail")
                self.lg.Click_Menu_Button()
                self.lg.Click_Logout_Button()
                self.lg.Login_Link()

            elif self.exp_result == "Login_Fail" and self.lg.Verify_Login_Status() == "Fail":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
                XLUTILIES.read_write(self.path, 'sheet1', r, 4, "Login_Fail")
                Result_List.append("Pass")
                self.lg.Login_Link()


        if "Fail" not in Result_List:
            self.log.info("Testcase test_user_login_DDT_002 is Pass")
            assert True
        else:
            self.log.info("Testcase test_user_login_DDT_002 is Fail")
            assert False
        self.log.info("Testcase test_user_login_DDT_002 is Completed")

