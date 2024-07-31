import logging
import random
import string


import pytest
from selenium.webdriver.common.by import By
from PageObjects.RegistrationPage import Registration_Class
from Utilities.Logger import Logging_Class
def Generate_Email():
    Email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{Email}@{domain}"

class Test_Registration:

    log = Logging_Class.log_generator()

    @pytest.mark.reg
    def test_registration(self, setup):
        self.gen_email = Generate_Email()
        self.log.info("Invoke browser")
        self.driver = setup
        self.reg = Registration_Class(self.driver)
        self.log.info("Enter URL")
        self.reg.click_on_register_link()
        self.log.info("enter name")
        self.reg.enter_reg_name("nik")
        self.log.info("enter email id")
        self.reg.enter_reg_email(self.gen_email)
        self.log.info("enter password")
        self.reg.enter_reg_password("Nik@123")
        self.log.info("enter confirm password")
        self.reg.enter_reg_confirm_password("Nik@123")
        self.log.info("click on register button")
        self.reg.click_on_reg_button()
        self.log.info("validate registration")

        if self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']").text == "CredKart":
            self.log.info("Registration pass")
            assert True
        else:
            self.log.info("Registration fail")
            assert False



