__author__ = 'ningxinliao'
import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.registration import Registration
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
import unidecode

class TestAccount(ProjectBase):
    REGISTRATION_PAGE = 'https://southwire-configurator-test.firebaseapp.com/register'

    def __init__(self, *args, **kwargs):
        super(TestAccount, self).__init__(*args, **kwargs)
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
        randomName = self.registration.generateRandomName()
        self.registration.enterContactName(randomName)
        sleep(2)
        self.registration.tapSubmit()
        sleep(5)
        expectedName = self.registration.getAccountName()

        self.assertion.assertEqual(expectedName, randomName)

    @pytest.mark.ac
    def testEditCompanyNameField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        randomCompanyName = self.registration.generateRandomCompanyName()
        self.registration.enterCompanyName(randomCompanyName)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getCompanyName().getValue()

        self.assertion.assertEqual(newValue,randomCompanyName)

    @pytest.mark.ac
    def testEditRoleField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        role = self.registration.generateRandomRole()
        self.registration.selectContactRole(role)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getSelectedRole()

        self.assertion.assertEqual(newValue,role)

    @pytest.mark.ac
    def testEditCityField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        randomCity = self.registration.generateRandomCity()
        self.registration.enterCity(randomCity)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getCity().getValue()

        self.assertion.assertEqual(newValue, randomCity)

    @pytest.mark.ac
    def testEditUSStateField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        state = self.registration.generateRandomState()
        self.registration.selectStateOrProvince(state)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getSelectedStateOrProvince()

        self.assertion.assertEqual(newValue, state)

    @pytest.mark.ac1
    def testEditCanadaProvinceField(self):
        email = 'khai.le+SWCA1@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        province = self.registration.generateRandomProvince()
        self.registration.selectStateOrProvince(province)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getSelectedStateOrProvince()

        self.assertion.assertEqual(newValue, province)

    @pytest.mark.ac
    def testEditZipField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        zip = self.registration.generateRandomZip()
        self.registration.enterZipCode(zip)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getZip().getValue()

        self.assertion.assertEqual(newValue, zip)

    @pytest.mark.ac
    def testEditPhoneField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'
    
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        phone = self.registration.generateRandomPhone()
        self.registration.enterPhoneNumber(phone)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getPhone().getValue()

        self.assertion.assertEqual(newValue, phone)

    @pytest.mark.ac
    def testEditUOMField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        uom = self.registration.generateRandomUnitOfMeasure()
        self.registration.selectUnitOfMeasure(uom)
        sleep(2)
        self.registration.tapSubmit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.navigation.navigateToAccountPage()
        sleep(2)
        newValue = self.registration.getSelectedUnitOfMeasure()

        self.assertion.assertEqual(newValue, uom)


    @pytest.mark.ac
    def testSouthwireEmployeeCannotEditRole(self):
        email = 'ningxin.liao+sw@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)

        el = self.registration.getRolePicker()
        self.assertion.assertFalse(el.ui_object.is_enabled())

        expectedRole = 'Southwire Employee'
        actualRole = self.registration.getSelectedRole()
        self.assertion.assertEqual(expectedRole, actualRole)

