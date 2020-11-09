import os


class Config:

    HOME_PAGE_URL = 'https://clarity.dexcom.com/'
    CHROME_EXECUTABLE_PATH = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
    CLINICAL_USERNAME = 'codechallenge'
    CLINICAL_PASSWORD = 'Password123'
    # logged in user name
    LOGGED_IN_CLINICAL_USER_NAME = 'Dexcom PA'