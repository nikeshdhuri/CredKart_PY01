from selenium.webdriver.common.by import By



class Registration_Class:

    register_link_xpath = (By.XPATH, "//a[normalize-space()='Register']")
    name_textbox_xpath = (By.XPATH, "//input[@id='name']")
    email_textbox_xpath = (By.XPATH, "//input[@id='email']")
    password_textbox_xpath = (By.XPATH, "//input[@id='password']")
    confirm_password_xpath = (By.XPATH, "//input[@id='password-confirm']")
    register_button_xpath = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_register_link(self):
        self.driver.find_element(*Registration_Class.register_link_xpath).click()


    def enter_reg_name(self, name):
        self.driver.find_element(*Registration_Class.name_textbox_xpath).send_keys(name)

    def enter_reg_email(self, email):
        self.driver.find_element(*Registration_Class.email_textbox_xpath).send_keys(email)

    def enter_reg_password(self, password):
        self.driver.find_element(*Registration_Class.password_textbox_xpath).send_keys(password)

    def enter_reg_confirm_password(self, confirm_password):
        self.driver.find_element(*Registration_Class.confirm_password_xpath).send_keys(confirm_password)

    def click_on_reg_button(self):
        self.driver.find_element(*Registration_Class.register_button_xpath).click()
