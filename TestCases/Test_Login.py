import logging

import pytest
from selenium.webdriver.common.by import By
from PageObjects.UserprofilePage import User_profile
from Utilities.Readproperties import ReadconfigClass
from Utilities.Logger import Logging_Class

@pytest.mark.usefixtures("setup")
@pytest.mark.loginclass
class Test_Login:
    email = ReadconfigClass.get_email_id()
    password = ReadconfigClass.get_password()
    invalid_password = ReadconfigClass.get_invalid_password()
    log = Logging_Class.log_generator()

    @pytest.mark.smoke
    def test_login001(self,setup):

        self.log.info("open browser")
        self.driver = setup
        self.log.info("click on login")
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
        self.log.info("enter email id")
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(self.email)
        self.log.info("enter password")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(self.password)
        self.log.info("click on login button")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        self.log.info("verify login")
        validation = self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']").text

        if validation == "CredKart":
            self.log.info("login pass")
            print(validation)
            print("Login pass")
            assert True
        else:
            print("Login fail")
            self.log.info("login fail")
            assert False

    @pytest.mark.retesting
    def test_login002(self,setup):
        self.log.info("Test case start")

        self.log.info("opening browser")
        self.driver = setup
        self.ur = User_profile(self.driver)
        self.log.info("click on logi link")
        self.ur.click_login_link()
        self.log.info("Enter Email id")
        self.ur.enter_email(self.email)
        self.log.info("Enter password")
        self.ur.enter_password(self.invalid_password)
        self.log.info("click on login button")
        self.ur.click_login_button()
        self.log.info("check login pass or fail")
        validation = self.ur.validate_login()

        if validation == "pass":
            self.log.info("login successful with invalid input")
            print(validation)
            self.driver.save_screenshot(".\\Screenshots\\login_fail_TC_fail1.PNG")
            assert False

        else:
            self.log.critical("login fail")
            self.driver.save_screenshot(".\\Screenshots\\login_fail_TC_pass1.PNG")
            assert True


####pytest -v --browser chrome -m loginclass --html=HtmlReports/log.html  --alluredir="C:\Users\Lenovo\Credkart_Project\AllureReports"