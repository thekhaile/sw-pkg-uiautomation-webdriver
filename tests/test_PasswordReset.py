from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.passwordReset import PasswordReset

class TestAuthentication(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestAuthentication, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.passwordReset = PasswordReset(self)

    @pytest.mark.ac
    def testResetAnExistingAccount(self):
        email = 'mmqaautomation@gmail.com'

        self.caseId = 1301644
        self.navigation.navigateToLoginPage()
        sleep(2)
        self.authentication.tapForgotPassword()
        sleep(2)
        self.passwordReset.enterEmail(email)
        self.passwordReset.tapReset()
        sleep(2)
        actualMsg = self.authentication.getConfirmationMsg()
        expectedMsg = 'Password reset sent. Please check your email and follow the link to reset your password.Resend password reset email.'

        self.assertion.assertEqual(actualMsg, expectedMsg)

    @pytest.mark.ac
    def testResetAnNonExistingAccount(self):
        email = 'automation@gmail.com'

        self.caseId = 1301646
        self.navigation.navigateToLoginPage()
        sleep(2)
        self.authentication.tapForgotPassword()
        sleep(2)
        self.passwordReset.enterEmail(email)
        self.passwordReset.tapReset()
        sleep(2)
        actualMsg = self.authentication.getConfirmationMsg()
        expectedMsg = 'Password reset sent. Please check your email and follow the link to reset your password.Resend password reset email.'

        self.assertion.assertEqual(actualMsg, expectedMsg)

    @pytest.mark.ac
    def testResetAnInvalidEmailFormat(self):
        email = 'automation'

        self.caseId = 1301645
        self.navigation.navigateToLoginPage()
        sleep(2)
        self.authentication.tapForgotPassword()
        sleep(2)
        self.passwordReset.enterEmail(email)
        self.passwordReset.tapReset()
        sleep(2)
        expectedURL = 'https://southwire-configurator-test.firebaseapp.com/reset-password'

        self.assertion.assertEqual(expectedURL, self.driver.current_url)
