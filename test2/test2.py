import unittest
import requests


class Test2(unittest.TestCase):

    def setUp(self):
        self.start_url = 'https://clarity.dexcom.com/users/auth/dexcom_sts/callback'
        self.session_analysis_url = 'https://clarity.dexcom.com/api/subject/1681277794575765504/analysis_session'
        self.credentials = {
            'username': 'codechallenge',
            'password': "Password123"
        }

    def test_login_clarity_dexcom(self):
        session = requests.Session()
        response = session.get(self.start_url)
        assert response.status_code == 200
        # initial url will redirected to new one.
        redirected_url = response.url
        response = session.get(redirected_url, data=self.credentials)
        assert response.status_code == 200
        response = session.get(self.session_analysis_url, data=self.credentials)
        assert response.status_code == 200



