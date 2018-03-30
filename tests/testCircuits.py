__author__ = 'ningxinliao'
import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects
from southwire_pkg_uiautomation_webdriver.components.jobs import Jobs
from southwire_pkg_uiautomation_webdriver.components.circuits import Circuits
from southwire_pkg_uiautomation_webdriver.components.feederSchedule import FeederSchedule
import unidecode

class TestCircuits(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestCircuits, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)
        self.jobs = Jobs(self)
        self.circuits = Circuits(self)
        self.feederSchedule = FeederSchedule(self)

    # TEST SCR-28 Add Circuit to Feeder Schedule

    @pytest.mark.ac
    def testCreateCircuitWithOnlyRequiredFieldsForUS(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311233
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.circuits.getCircuitFrom(rowOrder=0)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateCircuitWithOnlyRequiredFieldsForCanada(self):
        email = 'khai.le+SWCA1@mutualmobile.com'
        password = 'password'

        self.caseId = 1311234
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / RWU')
        sleep(1)
        self.circuits.selectConductorSize(size='350')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.circuits.getCircuitFrom(rowOrder=0)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateCircuitWithAllFields(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381368
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.toggleSIMpullHead()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.circuits.getCircuitFrom(rowOrder=0)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitCreateCircuitProcess(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311337
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.tapCancel()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Error Msg
    @pytest.mark.ac
    def testSIMpullHeadIsNotAvailableForSizes6Conductors(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='6')
        sleep(1)
        expectedErrorMsg = 'Heads cannot be applied to size 6 or 8.'
        actualErrorMsg = self.circuits.getErrorMsg()

        self.assertion.assertTrue(expectedErrorMsg in actualErrorMsg)

        el = self.circuits.getSIMpullHeadToggle()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testSIMpullHeadIsNotAvailableForSizes8Conductors(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311246
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='8')
        sleep(1)
        expectedErrorMsg = 'SIMpull (tm) Heads cannot be applied to size 6 or 8.'
        actualErrorMsg = unidecode.unidecode(self.circuits.getErrorMsg())

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)

        el = self.circuits.getSIMpullHeadToggle()
        self.assertion.assertFalse(el.isEnabled())

    # Missing Required Fields
    @pytest.mark.ac
    def testCreateCircuitWithoutFrom(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311341
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutTo(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378867
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutTypeAndSizeAndColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378868
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutSizeAndColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378869
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutLength(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378870
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutNumberOfConductorAndColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378871
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378872
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    # create circuit with long text
    @pytest.mark.ac
    def testMaxCharacterLimitInTheFromFieldOfCreateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311275
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterFrom('Far far away, behind')
        sleep(1)
        expectedText = 'Far far away, b'
        actualText = self.circuits.getFrom().getValue()

        self.assertion.assertEqual(expectedText, actualText)

        el = self.circuits.getSubmitButton()
        self.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testMaxCharacterLimitInTheToFieldOfCreateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311288
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterTo('Far far away, behind')
        sleep(1)
        expectedText = 'Far far away, b'
        actualText = self.circuits.getTo().getValue()

        self.assertion.assertEqual(expectedText, actualText)

        el = self.circuits.getSubmitButton()
        self.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testMaxCharacterLimitInTheLengthFieldOfCreateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311297
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterCircuitLength('1234567')
        sleep(1)
        expectedText = '123456'
        actualText = self.circuits.getLength().getValue()

        self.assertion.assertEqual(expectedText, actualText)

        el = self.circuits.getSubmitButton()
        self.assertFalse(el.isEnabled())

    '''Edit circuit'''

    @pytest.mark.ac
    def testEditFromField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        self.circuits.tapOverflow()
        sleep(3)
        self.circuits.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.circuits.getCircuitFrom()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditToField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(2)
        oldValue = self.circuits.getCircuitTo(rowOrder=0)
        self.circuits.tapOverflow()
        sleep(3)
        self.circuits.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.circuits.getCircuitTo(rowOrder=0)

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditTypeAndPreset(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        # end of precondition
        self.circuits.tapOverflow()
        sleep(3)
        self.circuits.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuits.selectConductorType(type='CU / XHHW')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(2)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditSizeAndPreset(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        oldValue = self.circuits.getCircuitSize()
        # end of precondition
        self.circuits.tapOverflow()
        sleep(3)
        self.circuits.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuits.selectConductorSize(size='1/0')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(2)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.circuits.getCircuitSize()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditLength(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        oldValue = self.circuits.getCircuitLength()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.circuits.getCircuitLength()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditSIMpullHead(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuits.toggleSIMpullHead()
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditNumberOfConductor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuits.selectNumOfConductor(NOC='3')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Brown-Orange-Yellow')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuits.tapSelectedColorCircle(circleOrder=0)
        sleep(1)
        self.circuits.selectColorOption(color='Black')
        sleep(1)
        self.circuits.tapSelectedColorCircle(circleOrder=1)
        sleep(1)
        self.circuits.selectColorOption(color='Black')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitEditCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuits.tapCancel()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testDeleteCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378723
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        # end of precondition
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDeleteCircuit()
        sleep(2)
        self.circuits.tapConfirmDelete()
        sleep(2)
        newValue = self.circuits.getCircuitFrom(rowOrder=0)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber + 1)
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testCancelDeleteCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378729
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        # end of precondition
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDeleteCircuit()
        sleep(2)
        self.circuits.tapCancelDelete()
        sleep(2)
        newValue = self.circuits.getCircuitFrom(rowOrder=0)
        sleep(3)

        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testDuplicateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376306
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        # end of precondition
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDuplicateCircuit()
        sleep(2)
        newValue = self.circuits.getCircuitFrom(rowOrder=1)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testEditDuplicatedCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376311
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDuplicateCircuit()
        sleep(2)
        # end of precondition
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapEditCircuit()
        sleep(2)
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.tapSubmit()
        sleep(2)
        newValue = self.circuits.getCircuitFrom(rowOrder=1)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testDeleteDuplicatedCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376312
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDuplicateCircuit()
        sleep(2)
        # end of precondition
        oldValue = self.circuits.getNumberOfRows()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDeleteCircuit()
        sleep(2)
        self.circuits.tapConfirmDelete()
        sleep(2)
        newValue = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldValue, newValue + 1)

    @pytest.mark.ac
    def testDuplicateDuplicatedCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376313
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuits.enterRandomFrom()
        sleep(1)
        self.circuits.enterRandomTo()
        sleep(1)
        self.circuits.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterRandomLength()
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDuplicateCircuit()
        sleep(2)
        # end of precondition
        oldValue = self.circuits.getCircuitFrom(rowOrder=0)
        self.circuits.tapOverflow()
        sleep(2)
        self.circuits.tapDuplicateCircuit()
        sleep(2)
        newValue = self.circuits.getCircuitFrom(rowOrder=1)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 2)
        self.assertion.assertEqual(oldValue, newValue)



