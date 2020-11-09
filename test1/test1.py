import unittest
from selenium import webdriver

from test1.config import Config
from test1.pages import StartPage, HomePage, LoginPage


class Test1(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(Config.CHROME_EXECUTABLE_PATH, options=chrome_options)
        self.driver.maximize_window()

    def test1(self):
        # go to home and click on dexcom clarity home users
        self.start_page = StartPage(self.driver)
        self.start_page.click_on_clinical_user_button()
        self.login_page = LoginPage(self.driver)
        self.login_page.login_clinical_users()
        self.home_page = HomePage(self.driver)
        self.home_page.check_whether_user_logged_in()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
