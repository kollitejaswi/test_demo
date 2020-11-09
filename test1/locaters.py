from selenium.webdriver.common.by import By


class Locaters:

    # home page locaters
    CLARITY_FOR_HOME_USERS = (By.LINK_TEXT, 'Dexcom CLARITY for Home Users')

    # login page locaters
    USER_NAME_TEXT_BOX = (By.ID, 'username')
    PASSWORD_TEXT_BOX = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'form-submit')

    # logged in user name
    LOGGED_IN_USER_NAME = (By.CLASS_NAME, 'home-user-header__name')


