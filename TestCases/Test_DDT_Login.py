# import pytest
# from PageObjects.UserprofilePage import User_profile
# from Utilities.Logger import Logging_Class
# from Utilities import ExcelFileOperation
import time

# class Test_login_DDT:
#     log = Logging_Class.log_generator()
#     path = "C:\\Users\\Lenovo\\Credkart_Project\\TestData\\LoginData.xlsx"
#
#     @pytest.mark.ddt
#     def test_login_DDT_004(self, setup):
#         self.log.info("Test case start")
#         self.log.info("opening browser")
#         self.driver = setup
#         self.ur = User_profile(self.driver)
#         self.log.info("click on logi link")
#         self.ur.click_login_link()
#
#         self.row = ExcelFileOperation.row_count(self.path, 'sheet1')
#         result_list = []
#
#         for r in range(2, self.row + 1):
#             self.email = ExcelFileOperation.read_data(self.path, 'sheet1', r, 1)
#             self.password = ExcelFileOperation.read_data(self.path, 'sheet1', r, 2)
#             self.Expected_Result = ExcelFileOperation.read_data(self.path, 'sheet1', r, 3)
#
#             self.log.info("Enter Email id")
#             self.ur.enter_email(self.email)
#             self.log.info("Enter password")
#             self.ur.enter_password(self.password)
#             self.log.info("click on login button")
#             self.ur.click_login_button()
#             self.log.info("check login pass or fail")
#
#             # validation = self.ur.validate_login()
#
#             if self.ur.validate_login() == "pass" and self.Expected_Result == "pass":
#                 self.log.info("login successful, TC pass")
#                 self.driver.save_screenshot(".\\Screenshots\\login_pass_TC_pass.PNG")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "pass")
#                 result_list.append("pass")
#
#                 self.ur.Click_Menu_Button()
#                 self.ur.Click_Logout_Button()
#                 self.ur.click_login_link()
#
#
#
#             elif self.ur.validate_login() == "pass" and self.Expected_Result == "fail":
#                 self.log.info("TC fail")
#                 self.driver.save_screenshot(".\\Screenshots\\login_pass_TC_fail.PNG")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "fail")
#                 result_list.append("fail")
#                 self.ur.click_login_link()
#
#
#             elif self.ur.validate_login() == "fail" and self.Expected_Result == "fail":
#                 self.log.info("TC pass")
#                 self.driver.save_screenshot(".\\Screenshots\\login_fail_TC_pass.PNJ")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "pass")
#                 result_list.append("pass")
#                 self.ur.click_login_link()
#
#
#             elif self.ur.validate_login() == "fail" and self.Expected_Result == "pass":
#                 self.log.info("TC fail")
#                 self.driver.save_screenshot(".\\Screenshots\\login_fail_TC_fail.PNJ")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "fail")
#                 result_list.append("fail")
#                 self.ur.click_login_link()
#
#         if "fail" in result_list:
#
#             assert True
#
#         else:
#
#             assert False
#
# ########################################################################################################

# import pytest
#
# from PageObjects.UserprofilePage import User_profile
# from Utilities.Logger import Logging_Class
# from Utilities import ExcelFileOperation
#
#
# class Test_Login_DDT:
#
#     log = Logging_Class.log_generator()
#     path = "C:\\Users\\Lenovo\\Credkart_Project\\TestData\\LoginData.xlsx"
#
#     @pytest.mark.ddt2
#     def test_CredKart_url_DDT_002(self, setup):
#         self.log.info("Testcase test_CredKart_url_DDT_002 is started")
#         self.log.info("Opening browser")
#         self.driver = setup
#         self.lg = User_profile(self.driver)
#         self.log.info("Click On login Link")
#         self.lg.click_login_link()
#         self.rows = ExcelFileOperation.row_count(self.path,'sheet1')
#         result_list = []
# # 5
#         for r in range(2, self.rows+1):
#
#             self.Email = ExcelFileOperation.read_data(self.path,'sheet1', r,1)
#             self.Password = ExcelFileOperation.read_data(self.path, 'sheet1', r, 2)
#             self.exp_result = ExcelFileOperation.read_data(self.path, 'sheet1', r, 3)
#
#             self.log.info("Enter Email" + self.Email)
#             self.lg.enter_email(self.Email)
#             self.log.info("Enter Password" + self.Password)
#             self.lg.enter_password(self.Password)
#             self.log.info("Click Login Button")
#             self.lg.click_login_button()
#             self.log.info("Verify Login Stauts")
#
#             if  self.exp_result == "Login_Pass" and self.lg.validate_login() == "Pass" :
#                 self.log.info("Taking screenshot")
#                 self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Pass")
#                 result_list.append("Pass")
#                 time.sleep(2)
#                 self.lg.click_menu_button()
#                 self.lg.click_logout_button()
#                 self.lg.click_login_link()
#
#
#             elif self.exp_result == "Login_Pass" and self.lg.Verify_Login_Status() == "Fail" :
#                 self.log.info("Taking screenshot")
#                 self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Fail")
#                 result_list.append("Fail")
#                 self.lg.click_login_link()
#
#             elif self.exp_result == "Login_Fail" and self.lg.Verify_Login_Status() == "Pass" :
#                 self.log.info("Taking screenshot")
#                 self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Fail")
#                 result_list.append("Fail")
#                 self.lg.Click_Menu_Button()
#                 self.lg.Click_Logout_Button()
#                 self.lg.click_login_link()
#
#
#             elif self.exp_result == "Login_Fail" and self.lg.validate_login() == "Fail":
#                 self.log.info("Taking screenshot")
#                 self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
#                 ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Fail")
#                 result_list.append("Pass")
#                 self.lg.click_login_link()
#
#
#         if "Fail" in result_list:
#             self.log.info("Testcase test_user_login_DDT_002 is Fail")
#             assert False
#         else:
#             self.log.info("Testcase test_user_login_DDT_002 is Pass")
#             assert True
#         self.log.info("Testcase test_user_login_DDT_002 is Completed\n")
#
#
##############################################################################################################


import pytest

from PageObjects.UserprofilePage import User_profile
from Utilities.Logger import Logging_Class
from Utilities import ExcelFileOperation


class Tes_Login_DDT:
    log = Logging_Class.log_generator()
    path = "C:\\Users\\Lenovo\\Credkart_Project\\TestData\\LoginData.xlsx"

    @pytest.mark.regression1
    def test_CredKart_url_DDT_001(self, setup):
        self.log.info("Testcase test_CredKart_url_DDT_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = User_profile(self.driver)
        self.log.info("Click On login Link")
        self.lg.click_login_link()
        self.rows = ExcelFileOperation.row_count(self.path, 'sheet1')
        result_list = []
        # 5
        for r in range(2, self.rows + 1):
            print("Loop Number --> " + str(r))
            self.Email = ExcelFileOperation.read_data(self.path, 'sheet1', r, 1)
            self.Password = ExcelFileOperation.read_data(self.path, 'sheet1', r, 2)
            self.exp_result = ExcelFileOperation.read_data(self.path, 'sheet1', r, 3)

            self.log.info("Enter Email" + self.Email)
            self.lg.enter_email(self.Email)
            self.log.info("Enter Password" + self.Password)
            self.lg.enter_password(self.Password)
            self.log.info("Click Login Button")
            self.lg.click_login_button()
            self.log.info("Verify Login Stauts")

            if self.exp_result == "Login_Pass" and self.lg.validate_login() == "Pass":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
                ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Pass")
                result_list.append("Pass")
                self.lg.click_menu_button()
                self.lg.click_logout_button()
                self.lg.click_login_link()


            elif self.exp_result == "Login_Pass" and self.lg.validate_login() == "Fail":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
                ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Fail")
                result_list.append("Fail")
                self.lg.click_login_link()


            elif self.exp_result == "Login_Fail" and self.lg.validate_login() == "Pass":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
                ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Fail")
                result_list.append("Fail")
                self.lg.click_menu_button()
                self.lg.click_logout_button()
                self.lg.click_login_link()


            elif self.exp_result == "Login_Fail" and self.lg.validate_login() == "Fail":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
                ExcelFileOperation.write_data(self.path, 'sheet1', r, 4, "Login_Fail")
                result_list.append("Pass")
                self.lg.click_login_link()

        print(result_list)
        if "Fail" in result_list:
            self.log.info("Testcase test_user_login_DDT_002 is Fail")
            assert False
        else:
            self.log.info("Testcase test_user_login_DDT_002 is Pass")
            assert True
        self.log.info("Testcase test_user_login_DDT_002 is Completed\n")
