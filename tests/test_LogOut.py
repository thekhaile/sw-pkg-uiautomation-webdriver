import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.registration import Registration


class TestLogOut(ProjectBase):
    LOGIN_PAGE = 'https://southwire-configurator-test.firebaseapp.com/login'

    def __init__(self, *args, **kwargs):
        super(TestLogOut, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.registration = Registration(self)

    @pytest.mark.ac
    def testSuccessfulLogOut(self):
        email = 'khai.le+SW1@mutualmobile.com'
        password = 'password'

        self.caseId = 1301623
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(1)
        self.navigation.navigateToAccountPage()
        sleep(2)
        self.registration.tapLogOut()
        sleep(2)
        currentUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, self.navigation.LOGIN_PAGE)

    @pytest.mark.ac
    def testAccountNotAccessibleOnceLoggedOut(self):
        email = 'khai.le+SW1@mutualmobile.com'
        password = 'password'

        self.caseId = 1301624
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(1)
        self.navigation.navigateToAccountPage()
        sleep(2)
        self.registration.tapLogOut()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        currentUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, self.navigation.LOGIN_PAGE)

    @pytest.mark.ac
    def testSuccessfulLogInAfterLogOut(self):
        email = 'khai.le+SW1@mutualmobile.com'
        password = 'password'

        self.caseId = 1301626
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(1)
        self.navigation.navigateToAccountPage()
        sleep(2)
        self.registration.tapLogOut()
        sleep(2)
        self.authentication.login(email, password)
        currentUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, self.navigation.LOGIN_PAGE)