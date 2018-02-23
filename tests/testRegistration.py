# import sys, os
# from time import sleep
# from projectBase import ProjectBase
# import pytest
# from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
# from southwire_pkg_uiautomation_webdriver.components.registration import Registration
# from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
#
#
# class TestRegistration(ProjectBase):
#     REGISTRATION_PAGE = 'https://southwire-configurator-test.firebaseapp.com/XXXXX'
#
#     def __init__(self, *args, **kwargs):
#         super(TestRegistration, self).__init__(*args, **kwargs)
#         self.authentication = Authentication(self)
#         self.navigation = Navigation(self)
#         self.registration = Registration(self)
#
#     @pytest.mark.ac
#     def testCreateAccountWithValidInfoForUS(self):
#         self.navigation.navigateToRegistrationPage()
#         sleep(1)
#         currentUrl = self.driver.current_url
#         self.registration.enterEmail()
#         sleep(1)
#         self.registration.enterPassword()
#         sleep(1)
#         self.registration.enterConfirmPassword()
#         sleep(1)
#         self.registration.enterContactName()
#         sleep(1)
#         self.registration.enterCompanyName()
#         sleep(1)
#         self.registration.selectContactRole()
#         sleep(1)
#         self.registration.enterAddress()
#         sleep(1)
#         self.registration.enterCity()
#         sleep(1)
#         self.registration.selectStateOrProvince()
#         sleep(1)
#         self.registration.enterZipCode()
#         sleep(1)
#         self.registration.enterPhoneNumber()
#         sleep(1)
#         self.registration.tapSubmit()
#         newUrl = self.driver.current_url
#
#         self.assertion.assertNotEqual(currentUrl, newUrl)
#
#     @pytest.mark.ac
#     def testExitRegistrationProcess(self):
#         self.navigation.navigateToRegistrationPage()
#         sleep(1)
#         currentUrl = self.driver.current_url
#         self.registration.enterEmail()
#         sleep(1)
#         self.registration.tapCancel()
#         newUrl = self.driver.current_url
#
#         self.assertion.assertNotEqual(currentUrl, newUrl)
#
#     def testCreateAccountWithSameEmail(self):
#         self.navigation.navigateToRegistrationPage()
#         sleep(1)
#         currentUrl = self.driver.current_url
#         self.registration.enterEmail('ningxin.liao@mutualmobile.com')
#         sleep(1)
#         self.registration.enterPassword('password')
#         sleep(1)
#         self.registration.enterConfirmPassword('password')
#         sleep(1)
#         self.registration.enterContactName()
#         sleep(1)
#         self.registration.enterCompanyName()
#         sleep(1)
#         self.registration.selectContactRole()
#         sleep(1)
#         self.registration.enterAddress()
#         sleep(1)
#         self.registration.enterCity()
#         sleep(1)
#         self.registration.selectStateOrProvince()
#         sleep(1)
#         self.registration.enterZipCode()
#         sleep(1)
#         self.registration.enterPhoneNumber()
#         sleep(1)
#         self.registration.tapSubmit()
#         newUrl = self.driver.current_url
#         expectedErrorMsg = 'Some Error'
#         actualErrorMsg = self.authentication.getErrorMsg()
#
#         self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
#         self.assertion.assertEqual(currentUrl, newUrl)
#
#
#
#     def testCreateAccountWithUnmatchPassword(self):
#         self.navigation.navigateToRegistrationPage()
#         sleep(1)
#         currentUrl = self.driver.current_url
#         self.registration.enterEmail('@mutualmobile.com')
#         sleep(1)
#         self.registration.enterPassword('password')
#         sleep(1)
#         self.registration.enterConfirmPassword('wrongpassword')
#         sleep(1)
#         self.registration.enterContactName()
#         sleep(1)
#         self.registration.enterCompanyName()
#         sleep(1)
#         self.registration.selectContactRole()
#         sleep(1)
#         self.registration.enterAddress()
#         sleep(1)
#         self.registration.enterCity()
#         sleep(1)
#         self.registration.selectStateOrProvince()
#         sleep(1)
#         self.registration.enterZipCode()
#         sleep(1)
#         self.registration.enterPhoneNumber()
#         sleep(1)
#         self.registration.tapSubmit()
#         newUrl = self.driver.current_url
#         expectedErrorMsg = 'Some Error'
#         actualErrorMsg = self.authentication.getErrorMsg()
#
#         self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
#         self.assertion.assertEqual(currentUrl, newUrl)
#
#
#     def testAssignSouthwireEmployeeRoleAutomatically(self):
#
#
#     def testLogInWithoutVerifyNewAcct(self):
#         email = 'unverified@mutualmobile.com'
#         password = 'password'
#
#         self.navigation.navigateToLoginPage()
#         currentUrl = self.driver.current_url
#         self.authentication.login(email, password)
#         newUrl = self.driver.current_url
#
#         self.assertion.assertNotEqual(currentUrl, newUrl)
#
#
#
#     # Error handling
#     def testCreateAcctWithoutEmail(self):
#
#
#
#
#     def testCreateAcctWithoutPassword(self):
#
#
#
#
#     def testCreateAcctWithoutConfirmPassword(self):
#
#
#
#
#     def testCreateAcctWithLessThan6CharPassword(self):
#
#
#
#
#     def testCreateAcctWithoutName(self):
#
#
#
#
#     def testCreateAcctWithoutRole(self):
#
#
#
#
#     def testCreateAcctWithoutCity(self):
#
#
#
#     def testCreateAcctWithoutState(self):
#
#
#
#
#     def testCreateAcctWithoutUOM(self):
#
#
#
#     def testZipCodeOver6AlpaCharMax(self):
#
#


















