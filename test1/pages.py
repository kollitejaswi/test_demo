from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test1.config import Config
from test1.locaters import Locaters


class BasePage(object):
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def write(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text


class StartPage(BasePage):
    """
    belongs to start page of the sit
    """

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.get(Config.HOME_PAGE_URL)

    def click_on_clinical_user_button(self):
        self.click(by_locator=Locaters.CLARITY_FOR_HOME_USERS)


class LoginPage(BasePage):
    """
    class for clinical user Login
    """

    def __init__(self, driver):
        super().__init__(driver=driver)

    def login_clinical_users(self):
        # enter clinical user credentials and login
        self.write(by_locator=Locaters.USER_NAME_TEXT_BOX, text=Config.CLINICAL_USERNAME)
        self.write(by_locator=Locaters.PASSWORD_TEXT_BOX, text=Config.CLINICAL_PASSWORD)
        self.click(by_locator=Locaters.LOGIN_BUTTON)


class HomePage(BasePage):
    """
    Home page after login
    """

    def __init__(self, driver):
        super().__init__(driver=driver)

    def check_whether_user_logged_in(self):
        # check whether user logged in success fully or not
        self.assert_element_text(by_locator=Locaters.LOGGED_IN_USER_NAME,
                                 element_text=Config.LOGGED_IN_CLINICAL_USER_NAME)
