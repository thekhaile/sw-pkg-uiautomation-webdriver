from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.registration import Registration
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
import unidecode


class TestRegistration(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestRegistration, self).__init__(*args, **kwargs)
        self.authentication = Authentication(self)
        self.navigation = Navigation(self)
        self.registration = Registration(self)

    @pytest.mark.ac
    def testCreateAccountWithValidInfoForUS(self):
        self.caseId = 1381580
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
        self.registration.selectRandomRole()
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
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateAccountWithValidInfoForCanada(self):
        self.caseId = 1381581
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
        self.registration.enterZipCode('H1A0A1')
        sleep(1)
        self.registration.enterPhoneNumber('418-999-9999')
        sleep(1)
        self.registration.selectUnitOfMeasure(UOM='Standard')
        sleep(1)
        self.registration.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateAccountWithAllFields(self):
        self.caseId = 1381582
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
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateAccountWithOnlyRequiredFields(self):
        self.caseId = 1381583
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
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitRegistrationProcess(self):
        self.caseId = 1307370
        self.navigation.navigateToLoginPage()
        sleep(3)
        currentUrl = self.driver.current_url
        self.registration.tapCreateAccount()
        self.registration.enterRandomEmail()
        sleep(3)
        self.registration.tapCancel()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testNavigateBackToLoginScreenAfterTapCancel(self):
        self.caseId = 1307377
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


    """Error handling"""
    @pytest.mark.ac
    def testCreateAccountWithSameEmail(self):
        self.caseId = 1307222
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
        sleep(2)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'This email address is already in use.'
        actualErrorMsg = self.registration.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateAccountWithUnmatchPassword(self):
        self.caseId = 1307223
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        currentUrl = self.driver.current_url
        self.registration.enterRandomEmail()
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        self.registration.enterConfirmPassword('Password')
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

    @pytest.mark.ac
    def testCreateAcctWithLessThan6CharPassword(self):
        self.caseId = 1307224
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

    @pytest.mark.ac
    def testAssignSouthwireEmployeeRoleAutomatically(self):
        self.caseId = 1307220
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterEmail('russ.king@southwire.com')
        sleep(1)

        el = self.registration.getRolePicker()
        # Get the Picker to work using Selenium's own library
        self.assertion.assertFalse(el.ui_object.is_enabled())

        expectedRole = 'Southwire Employee'
        actualRole = self.registration.getSelectedRole()
        self.assertion.assertEqual(expectedRole, actualRole)

    @pytest.mark.ac
    def testRegisterWithInvalidEmailFormat(self):
        self.caseId = 1307371
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

    """Error handling for required fields"""
    @pytest.mark.ac
    def testCreateAcctWithoutEmail(self):
        self.caseId = 1307231
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

    @pytest.mark.ac
    def testCreateAcctWithoutPassword(self):
        self.caseId = 1307245
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

    @pytest.mark.ac
    def testCreateAcctWithoutConfirmPassword(self):
        self.caseId = 1307258
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

    @pytest.mark.ac
    def testCreateAcctWithoutContactName(self):
        self.caseId = 1307270
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

    @pytest.mark.ac
    def testCreateAcctWithoutCompanyName(self):
        self.caseId = 1307284
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

    @pytest.mark.ac
    def testCreateAcctWithoutRole(self):
        self.caseId = 1381777
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

    @pytest.mark.ac
    def testCreateAcctWithoutCity(self):
        self.caseId = 1307298
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

    @pytest.mark.ac
    def testCreateAcctWithoutState(self):
        self.caseId = 1307326
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

    @pytest.mark.ac
    def testContactNameCanBeEntered(self):
        self.caseId = 1307200
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterContactName('Ningxin Liao')
        sleep(3)
        name = self.registration.getContactName().getValue()
        self.assertion.assertEqual(name, 'Ningxin Liao')

    @pytest.mark.ac
    def testCompanyNameCanBeEntered(self):
        self.caseId = 1307206
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterCompanyName('Mutual Mobile')
        sleep(1)
        companyName = self.registration.getCompanyName().getValue()
        self.assertion.assertEqual(companyName, 'Mutual Mobile')

    @pytest.mark.ac
    def testEmailCanBeEntered(self):
        self.caseId = 1307207
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterEmail('ningxin.test@mutalmobile.com')
        sleep(1)
        email = self.registration.getEmail().getValue()
        self.assertion.assertEqual(email, 'ningxin.test@mutalmobile.com')

    @pytest.mark.ac
    def testCityCanBeEntered(self):
        self.caseId = 1307209
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterCity('Austin')
        sleep(1)
        city = self.registration.getCity().getValue()
        self.assertion.assertEqual(city, 'Austin')

    @pytest.mark.ac
    def testZipCodeCanBeEntered(self):
        self.caseId = 1307212
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterZipCode('78701')
        sleep(1)
        zip = self.registration.getZip().getValue()
        self.assertion.assertEqual(zip, '78701')

    @pytest.mark.ac
    def testPhoneNumberCanBeEntered(self):
        self.caseId = 1307213
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterPhoneNumber('5120000000')
        sleep(1)
        phone = self.registration.getPhone().getValue()
        self.assertion.assertEqual(phone, '5120000000')

    @pytest.mark.ac
    def testPasswordCanBeEntered(self):
        self.caseId = 1307216
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterPassword('password')
        sleep(1)
        password = self.registration.getPassword().getValue()
        self.assertion.assertEqual(password, 'password')

    @pytest.mark.ac
    def testConfirmPasswordCanBeEntered(self):
        self.caseId = 1307218
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterConfirmPassword('password')
        sleep(1)
        condirmPassword = self.registration.getConfirmPassword().getValue()
        self.assertion.assertEqual(condirmPassword, 'password')

    @pytest.mark.ac
    def testSouthwireEmployeeRoleCanBeSelected(self):
        self.caseId = 1307201
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.selectContactRole(role='Southwire Employee')
        sleep(1)
        role = self.registration.getSelectedRole()
        self.assertion.assertEqual(role, 'Southwire Employee')

    @pytest.mark.ac
    def testSalesAgentRoleCanBeSelected(self):
        self.caseId = 1307203
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.selectContactRole(role='Sales/Agent')
        sleep(1)
        role = self.registration.getSelectedRole()
        self.assertion.assertEqual(role, 'Sales/Agent')

    @pytest.mark.ac
    def testOtherRoleCanBeSelected(self):
        self.caseId = 1307204
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.selectContactRole(role='Other')
        sleep(1)
        role = self.registration.getSelectedRole()
        self.assertion.assertEqual(role, 'Other')

    @pytest.mark.ac
    def testContractorRoleCanBeSelected(self):
        self.caseId = 1307202
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.selectContactRole(role='Contractor')
        role = self.registration.getSelectedRole()
        self.assertion.assertEqual(role, 'Contractor')

    @pytest.mark.ac
    def testStateProvinceCanBeSelected(self):
        self.caseId = 1307211
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.selectStateOrProvince(state='Texas')
        sleep(1)
        state = self.registration.getSelectedStateOrProvince()
        self.assertion.assertEqual(state, 'Texas')

    @pytest.mark.ac
    def testSTDUnitOfMeasureCanBeSelected(self):
        self.caseId = 1307214
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.selectUnitOfMeasure(UOM='Standard')
        sleep(1)
        uom = self.registration.getSelectedUnitOfMeasure()
        self.assertion.assertEqual(uom, 'Standard')

    @pytest.mark.ac
    def testMetricUnitOfMeasureCanBeSelected(self):
        self.caseId = 1307215
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.selectUnitOfMeasure(UOM='Metric')
        sleep(1)
        uom = self.registration.getSelectedUnitOfMeasure()
        self.assertion.assertEqual(uom, 'Metric')

    @pytest.mark.ac
    def testSouthwireEmployeeCannotModifyRole(self):
        self.caseId = 1307221
        self.navigation.navigateToRegistrationPage()
        sleep(1)
        self.registration.enterEmail('ningxin.test+sw@southwire.com')
        self.registration.selectContactRole(role='Other')
        role = self.registration.getSelectedRole()
        self.assertion.assertEqual(role, 'Southwire Employee')