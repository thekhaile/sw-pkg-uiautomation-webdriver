import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
from time import sleep
from projectBase import ProjectBase
import pytest
from sharedComponents.nagivation import Navigation
from sharedComponents.authentication import Authentication

class TestAuthentication(ProjectBase):
    LOGIN_PAGE = 'https://southwire-configurator-test.firebaseapp.com/login'

    def __init__(self, *args, **kwargs):
        super(TestAuthentication, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)

    @pytest.mark.sandbox
    @pytest.mark.ac
    def testSuccessfulLoginWithValidCredentials(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        sleep(5)
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testuserStaysLoggedInUponGoingBack(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.driver.back()
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testuserStaysLoggedInUponRefreshing(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.driver.refresh()
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testUnsuccessfulLoginWithIncorrectPassword(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password1234'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.assertion.assertEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testResubmitAfterFailedAttemptofWrongPassword(self):
        email = 'khai.le@mutualmobile.com'
        incorrectPassword = 'password1234'
        correctPassword = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(incorrectPassword)
        self.authentication.tapSubmit()
        self.authentication.enterPassword(correctPassword)
        self.authentication.tapSubmit()
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testResubmitAfterFailedAttemptofWrongEmail(self):
        inCorrectEmail = 'khai.le1@mutualmobile.com'
        correctEmail = 'khai.le@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(inCorrectEmail)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.authentication.enterEmail(correctEmail)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testUnsuccessfulLoginWithNonexistingEmail(self):
        email = 'noexist@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.assertion.assertEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.functionality
    def testSubmitButtonDisabledWhenEmailAndPasswordAreEmpty(self):
        self.navigation.navigateToLoginPage()
        el = self.app.findElement(self.app.getStrategy().XPATH,'//*[@id="root"]/div/main/div/div/form/button[1]')
        el = self.UIType.Button(el)
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.functionality
    def testSubmitButtonDisabledWhenEmailIsEmpty(self):
        password = 'password'
        self.navigation.navigateToLoginPage()
        self.authentication.enterPassword(password)
        el = self.app.findElement(self.app.getStrategy().XPATH,'//*[@id="root"]/div/main/div/div/form/button[1]')
        el = self.UIType.Button(el)
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.functionality
    def testSubmitButtonDisabledWhenPasswordIsEmpty(self):
        email = 'noexist@mutualmobile.com'
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        el = self.app.findElement(self.app.getStrategy().XPATH,'//*[@id="root"]/div/main/div/div/form/button[1]')
        el = self.UIType.Button(el)
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.functionality
    def testSubmitButtonEnabledWhenEmailAndPasswordAreFilledOut(self):
        email = 'noexist@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        el = self.app.findElement(self.app.getStrategy().XPATH,'//*[@id="root"]/div/main/div/div/form/button[1]')
        el = self.UIType.Button(el)
        self.assertion.assertTrue(el.isEnabled())