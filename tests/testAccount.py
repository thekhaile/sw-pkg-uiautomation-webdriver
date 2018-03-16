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

    # Edit Account Info
    @pytest.mark.ac
    def testEditNameField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.enterRandomName()
        sleep(2)
        realName = self.registration.getContactName().getValue()
        sleep(2)
        self.registration.tapSubmit()
        sleep(5)
        expectedName = self.registration.getAccountName()

        self.assertion.assertEqual(expectedName, realName)

    @pytest.mark.ac
    def testEditCompanyNameField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.enterRandomCompanyName()
        sleep(2)
        realName = self.registration.getCompanyName().getValue()
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        expectedName = self.registration.getCompanyName().getValue()

        self.assertion.assertEqual(expectedName, realName)

    @pytest.mark.ac
    def testEditRoleField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.selectRandomRole()
        sleep(2)
        actualRole = self.registration.getSelectedRole()
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        expectedRole = self.registration.getSelectedRole()
        self.assertion.assertEqual(expectedRole, actualRole)

    @pytest.mark.ac
    def testEditCityField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        oldValue = self.registration.getCity().getValue()
        randomCity = self.registration.generateRandomCity()
        self.registration.enterCity(randomCity)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        newValue = self.registration.getCity().getValue()
        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, randomCity)

    @pytest.mark.ac
    def testEditStateField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.selectRandomStateOrProvince()
        sleep(2)
        actualRole = self.registration.getStateOrProvince().getLabel()
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        expectedRole = self.registration.getStateOrProvince().getLabel()
        self.assertion.assertEqual(expectedRole, actualRole)

    @pytest.mark.ac
    def testEditZipField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.enterRandomZip()
        sleep(2)
        realResult = self.registration.getZip().getLabel()
        self.registration.tapSubmit()
        sleep(2)
        expectedResult = self.registration.getZip().getLabel()

        self.assertion.assertEqual(expectedResult, realResult)

    @pytest.mark.ac
    def testEditPhoneField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'
    
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.enterRandomPhone()
        sleep(2)
        realResult = self.registration.getPhone().getLabel()
        self.registration.tapSubmit()
        sleep(2)
        expectedResult = self.registration.getPhone().getLabel()

        self.assertion.assertEqual(expectedResult, realResult)

    @pytest.mark.ac
    def testEditUOMField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.selectRandomUnitOfMeasure()
        sleep(2)
        realResult = self.registration.getUnitOfMeasure().getLabel()
        self.registration.tapSubmit()
        sleep(2)
        expectedResult = self.registration.getUnitOfMeasure().getLabel()

        self.assertion.assertEqual(expectedResult, realResult)