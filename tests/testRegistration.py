__author__ = 'ningxinliao'
import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.registration import Registration
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication


class TestRegistration(ProjectBase):
    REGISTRATION_PAGE = 'https://southwire-configurator-test.firebaseapp.com/XXXXX'

    def __init__(self, *args, **kwargs):
        super(TestRegistration, self).__init__(*args, **kwargs)
        self.authentication = Authentication(self)
        self.navigation = Navigation(self)
        self.registration = Registration(self)

    @pytest.mark.ac
    def testCreateAccountWithValidInfoForUS(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+10@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword()
        sleep(1)
        self.registration.enterConfirmPassword()
        sleep(1)
        self.registration.enterContactName()
        sleep(1)
        self.registration.enterCompanyName()
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress()
        sleep(1)
        self.registration.enterCity()
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode()
        sleep(1)
        self.registration.enterPhoneNumber()
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitRegistrationProcess(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail()
        sleep(1)
        self.registration.tapCancel()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAccountWithSameEmail(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName()
        sleep(1)
        self.registration.enterCompanyName()
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress()
        sleep(1)
        self.registration.enterCity()
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode()
        sleep(1)
        self.registration.enterPhoneNumber()
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    def testCreateAccountWithUnmatchPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+11@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('wrongpassword')
        sleep(1)
        self.registration.enterContactName()
        sleep(1)
        self.registration.enterCompanyName()
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress()
        sleep(1)
        self.registration.enterCity()
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode()
        sleep(1)
        self.registration.enterPhoneNumber()
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    def testCreateAcctWithLessThan6CharPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('pass')
        sleep(1)
        self.registration.enterConfirmPassword('pass')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)


    def testAssignSouthwireEmployeeRoleAutomatically(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('russ.king@southwire.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName()
        sleep(1)
        self.registration.enterCompanyName()
        sleep(1)
        # self.registration.selectContactRole()
        # sleep(1)
        self.registration.enterAddress()
        sleep(1)
        self.registration.enterCity()
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode()
        sleep(1)
        self.registration.enterPhoneNumber()
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedRole = 'Southwire Employee'
        actualRole = self.registration.getContactRole()

        self.assertion.assertEqual(expectedRole, actualRole)
        self.assertion.assertEqual(currentUrl, newUrl)

    def testModifyRoleForSouthwireEmployeeEmail(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('russ.king@southwire.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName()
        sleep(1)
        self.registration.enterCompanyName()
        sleep(1)
        self.registration.selectContactRole('Other')
        sleep(1)
        self.registration.enterAddress()
        sleep(1)
        self.registration.enterCity()
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode()
        sleep(1)
        self.registration.enterPhoneNumber()
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    def testZipCodeOver6AlpaCharMax(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('7870107')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testLogInWithoutVerifyNewAcct(self):
        email = 'unverified@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        currentUrl = self.driver.current_url
        self.authentication.login(email, password)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testRegisterWithInvalidFormatEmail(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Error handling for required fields
    def testCreateAcctWithoutEmail(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        # self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        # sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAcctWithoutPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        # self.registration.enterPassword('password')
        # sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAcctWithoutConfirmPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        # self.registration.enterConfirmPassword('password')
        # sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAcctWithoutName(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        # self.registration.enterContactName('Ningxin Liao')
        # sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAcctWithoutRole(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        # self.registration.selectContactRole()
        # sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAcctWithoutCity(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        # self.registration.enterCity('Austin')
        # sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAcctWithoutState(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        # self.registration.selectStateOrProvince()
        # sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        self.registration.selectUnitOfMeasure()
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCreateAcctWithoutUOM(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('ningxin.liao+12@mutualmobile.com')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole()
        sleep(1)
        self.registration.enterAddress('301 Congress Ave')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('')
        sleep(1)
        # self.registration.selectUnitOfMeasure()
        # sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertNotEqual(currentUrl, newUrl)
    # End of required fields























