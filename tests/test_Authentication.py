import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
import unidecode

class TestAuthentication(ProjectBase):
    LOGIN_PAGE = 'https://southwire-configurator-test.firebaseapp.com/login'

    def __init__(self, *args, **kwargs):
        super(TestAuthentication, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)

    @pytest.mark.ac
    def testSuccessfulLoginWithValidCredentials(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.caseId = 1300685
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testuserStaysLoggedInUponGoingBack(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.caseId = 1300696
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.driver.back()
        sleep(5)
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testuserStaysLoggedInUponRefreshing(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.caseId = 1300693
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.driver.refresh()
        sleep(5)
        self.assertion.assertNotEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.ac
    def testUnsuccessfulLoginWithIncorrectPassword(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password1234'

        self.caseId = 1300690
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

        self.caseId = 1300691
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

        self.caseId = 1300689
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

        self.caseId = 1300687
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)
        self.authentication.tapSubmit()
        self.assertion.assertEqual(TestAuthentication.LOGIN_PAGE, self.driver.current_url)

    @pytest.mark.functionality
    def testSubmitButtonDisabledWhenEmailAndPasswordAreEmpty(self):
        self.caseId = 1381554
        self.navigation.navigateToLoginPage()
        el = self.authentication.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.functionality
    def testSubmitButtonDisabledWhenEmailIsEmpty(self):
        password = 'password'
        self.caseId = 1381555
        self.navigation.navigateToLoginPage()
        self.authentication.enterPassword(password)
        el = self.authentication.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.functionality
    def testSubmitButtonDisabledWhenPasswordIsEmpty(self):
        email = 'noexist@mutualmobile.com'
        self.caseId = 1381556
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        el = self.authentication.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.functionality
    def testSubmitButtonEnabledWhenEmailAndPasswordAreFilledOut(self):
        email = 'noexist@mutualmobile.com'
        password = 'password'

        self.caseId = 1300726
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail(email)
        self.authentication.enterPassword(password)

        el = self.authentication.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())

    @pytest.mark.ac
    def testLogInWithoutVerifyNewAcct(self):
        email = 'ningxin.liao+unverified@mutualmobile.com'
        password = 'password'

        self.caseId = 1381557
        self.navigation.navigateToLoginPage()
        currentUrl = self.driver.current_url
        self.authentication.login(email, password)
        newUrl = self.driver.current_url
        expectedErrorMsg = "This account hasn't been verified.Resend verification email."
        actualErrorMsg = unidecode.unidecode(self.authentication.getErrorMsg())

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.ac1
    def testMultipleFailedAttemptsAtLogin(self):
        email = 'khai.le+SW1@mutualmobile.com'
        password = 'passwor'

        self.caseId = 1300692
        self.navigation.navigateToLoginPage()
        currentUrl = self.driver.current_url
        for i in range(5):
            self.authentication.login(email, password)
            newUrl = self.driver.current_url
            expectedErrorMsg = "This email or password is incorrect."
            actualErrorMsg = unidecode.unidecode(self.authentication.getErrorMsg())
            self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
            self.assertion.assertEqual(currentUrl, newUrl)

