from selenium.webdriver.common.by import By


class User_profile:

    def __init__(self, driver):
        self.driver = driver

    login_link_xpath = "//a[normalize-space()='Login']"
    email_id_xpath = "//input[@id='email']"
    password_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@type='submit']"
    validation_xpath = "//h2[normalize-space()='CredKart']"
    invalid_login_xpath = "//strong[normalize-space()='These credentials do not match our records.']"
    Menu_Button_XPATH = "//a[@role='button']"
    Logout_Button_XPATH = "//a[normalize-space()='Logout']"

    def click_login_link(self):
        self.driver.find_element(By.XPATH, self.login_link_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_id_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def validate_login(self):
        try:
            self.driver.find_element(By.XPATH, self.validation_xpath)
            return  "pass"
        except:
            return "fail"

    def click_menu_button(self):
        self.driver.find_element(By.XPATH, self.Menu_Button_XPATH).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.Logout_Button_XPATH).click()


