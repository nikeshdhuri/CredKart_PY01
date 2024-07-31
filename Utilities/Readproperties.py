import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Lenovo\\Credkart_Project\\Configuration\\config.ini")


class ReadconfigClass:

    @staticmethod
    def get_login_url():
        login_url = config.get('user_info', 'login_url')
        return login_url

    @staticmethod
    def get_email_id():
        email = config.get('user_info', 'email_id')
        return email


    @staticmethod
    def get_password():
        password = config.get('user_info', 'password')
        return password

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('user_info', 'invalid_password')
        return invalid_password

