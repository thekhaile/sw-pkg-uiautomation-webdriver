__author__ = 'ningxinliao'
import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.registration import Registration
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
import unidecode


class TestRegistration(ProjectBase):
    REGISTRATION_PAGE = 'https://southwire-configurator-test.firebaseapp.com/register'

    def __init__(self, *args, **kwargs):
        super(TestRegistration, self).__init__(*args, **kwargs)
        self.authentication = Authentication(self)
        self.navigation = Navigation(self)
        self.registration = Registration(self)

    @pytest.mark.ac1
    # Verify
    def testCreateAccountWithValidInfoForUS(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('512-999-9999')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac2
    # Verify
    def testCreateAccountWithValidInfoForCanada(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        sleep(1)
        self.registration.enterCity('Montreal')
        sleep(1)
        self.registration.selectStateOrProvince(state='Quebec')
        sleep(1)
        self.registration.enterZipCode('A1A1A1')
        sleep(1)
        self.registration.enterPhoneNumber('418-999-9999')
        sleep(1)
        self.registration.selectUnitOfMeasure(UOM='Standard')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac8
    def testCreateAccountWithAllFields(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='California')
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        self.registration.enterPhoneNumber('512-999-9999')
        sleep(1)
        self.registration.selectUnitOfMeasure(UOM='Metric')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac3
    def testExitRegistrationProcess(self):
        self.navigation.navigateToRegistrationPage()
        sleep(3)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(3)
        self.registration.tapCancel()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac4
    def testNavigateBackToLoginScreenAfterTapCancel(self):
        self.navigation.navigateToLoginPage()
        sleep(2)
        currentUrl = self.driver.current_url
        self.authentication.tapCreateAccount()
        self.registration.enterRandomEmail()
        sleep(2)
        self.registration.tapCancel()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.ac5
    def testCreateAccountWithOnlyRequiredFields(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Quebec')
        sleep(1)
        self.registration.selectUnitOfMeasure(UOM='Standard')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac6
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
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'This email address is already in use.'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.ac7
    def testCreateAccountWithUnmatchPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('wrongpassword')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = "Your passwords don't match."
        actualErrorMsg = self.registration.getErrorMsg()
        actualErrorMsg = unidecode._unidecode(actualErrorMsg)

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.ac9
    def testCreateAcctWithLessThan6CharPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(1)
        self.registration.enterPassword('pass')
        sleep(1)
        self.registration.enterConfirmPassword('pass')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Password must be 6 or more characters.'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    # @pytest.mark.ac10
    # def testAssignSouthwireEmployeeRoleAutomatically(self):
    #     self.navigation.navigateToRegistrationPage()
    #     sleep(1)
    #     currentUrl = self.driver.current_url
    #     self.registration.enterEmail('russ.king@southwire.com')
    #     sleep(1)
    #     # self.registration.enterContactName('Russ King')
    #     # sleep(1)
    #     newUrl = self.driver.current_url
    #     expectedRole = 'Southwire Employee'
    #     actualRole = self.registration.getCurrentRole()
    #
    #     self.assertion.assertEqual(expectedRole, actualRole)
    #     self.assertion.assertEqual(currentUrl, newUrl)
    #
    #     el = self.registration.getRolePicker()
    #     # Get the Picker to work using Selenium's own library
    #     self.assertion.assertFalse(el.ui_object.is_enabled())

    @pytest.mark.ac11
    def testRegisterWithInvalidFormatEmail(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterEmail('InvalidFormat@mm')
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Distributor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'This email format is incorrect.'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    # Error handling for required fields
    @pytest.mark.ac12
    def testCreateAcctWithoutEmail(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Distributor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()

        newUrl = self.driver.current_url
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.registration.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac13
    def testCreateAcctWithoutPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Distributor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()

        newUrl = self.driver.current_url
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.registration.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac14
    def testCreateAcctWithoutConfirmPassword(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Distributor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()

        newUrl = self.driver.current_url
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.registration.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac15
    def testCreateAcctWithoutName(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Distributor')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()

        newUrl = self.driver.current_url
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.registration.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac16
    def testCreateAcctWithoutRole(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()

        newUrl = self.driver.current_url
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.registration.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac17
    def testCreateAcctWithoutCity(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Other')
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        self.registration.tapSubmit()

        newUrl = self.driver.current_url
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.registration.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac18
    def testCreateAcctWithoutState(self):
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(1)
        self.registration.enterCompanyName('MM')
        sleep(1)
        self.registration.selectContactRole(role='Other')
        sleep(1)
        self.registration.enterCity('Hot Springs')
        sleep(1)
        self.registration.tapSubmit()

        newUrl = self.driver.current_url
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.registration.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    # End of required fields























