import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
import unidecode


class TestCircuit(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestCircuit, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.jobList = JobList(self)
        self.job = Job(self)
        self.circuit = Circuit(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)

    @pytest.mark.ac
    def testCreateCircuitWithOnlyRequiredFieldsForUS(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311233
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        fromText = self.circuit.generateRandomFrom()
        self.circuit.enterFrom(fromText)
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertEqual(fromText, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateCircuitWithOnlyRequiredFieldsForCanada(self):
        email = 'khai.le+SWCA1@mutualmobile.com'
        password = 'password'

        self.caseId = 1311234
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """precondition"""
        self.job.createAJob()
        """end of precondition"""
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        fromText = self.circuit.generateRandomFrom()
        self.circuit.enterFrom(fromText)
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / RWU')
        sleep(1)
        self.circuit.selectConductorSize(size='350')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertEqual(fromText, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateCircuitWithAllFields(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381368
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """precondition"""
        self.job.createAJob()
        """end of precondition"""
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        fromText = self.circuit.generateRandomFrom()
        self.circuit.enterFrom(fromText)
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.toggleSIMpullHead()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertEqual(fromText, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitCreateCircuitProcess(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311337
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.tapCancel()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    """Error messages"""
    @pytest.mark.ac
    def testSIMpullHeadIsNotAvailableForSizes6Conductors(self):
        # Verify that SIMpull option is not available with size 6 circuit
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311238
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='6')
        sleep(1)
        expectedErrorMsg = 'SIMpull (tm) Heads cannot be applied to size 6 or 8.'
        actualErrorMsg = unidecode.unidecode(self.circuit.getErrorMsg())

        self.assertion.assertTrue(expectedErrorMsg in actualErrorMsg)

        el = self.circuit.getSIMpullHeadToggle()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testSIMpullHeadIsNotAvailableForSizes8Conductors(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311246
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='8')
        sleep(1)
        expectedErrorMsg = 'SIMpull (tm) Heads cannot be applied to size 6 or 8.'
        actualErrorMsg = unidecode.unidecode(self.circuit.getErrorMsg())

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)

        el = self.circuit.getSIMpullHeadToggle()
        self.assertion.assertFalse(el.isEnabled())

    """Missing required fields"""
    @pytest.mark.ac
    def testCreateCircuitWithoutFrom(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311341
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterCircuitLength('123')
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuit.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutTo(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378867
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterCircuitLength('123')
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuit.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutTypeAndSizeAndColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378868
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.enterCircuitLength('123')
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuit.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutSizeAndColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378869
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.enterCircuitLength('123')
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuit.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutLength(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378870
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuit.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutNumberOfConductorAndColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378871
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterCircuitLength('123')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuit.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378872
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuit.enterFrom('ABC123')
        sleep(1)
        self.circuit.enterTo('QWE098')
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterCircuitLength('123')
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuit.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    """Long texts"""
    @pytest.mark.ac
    def testMaxCharacterLimitInTheFromFieldOfCreateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311275
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterFrom('Far far away, behind')
        sleep(1)
        expectedText = 'Far far away, b'
        actualText = self.circuit.getFrom().getValue()

        self.assertion.assertEqual(expectedText, actualText)

        el = self.circuit.getSubmitButton()
        self.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testMaxCharacterLimitInTheToFieldOfCreateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311288
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterTo('Far far away, behind')
        sleep(1)
        expectedText = 'Far far away, b'
        actualText = self.circuit.getTo().getValue()

        self.assertion.assertEqual(expectedText, actualText)

        el = self.circuit.getSubmitButton()
        self.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testMaxCharacterLimitInTheLengthFieldOfCreateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311297
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterCircuitLength('1234567')
        sleep(1)
        expectedText = '123456'
        actualText = self.circuit.getLength().getValue()

        self.assertion.assertEqual(expectedText, actualText)

        el = self.circuit.getSubmitButton()
        self.assertFalse(el.isEnabled())

    """Edit Circuit"""

    @pytest.mark.ac
    def testEditFromField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376011
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        self.circuit.createLargeUSCircuit()
        sleep(3)
        oldValue = self.feederSchedule.getCircuitFrom()
        self.feederSchedule.tapOverflow()
        sleep(3)
        self.feederSchedule.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.feederSchedule.getCircuitFrom()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditToField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376012
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        self.circuit.createLargeUSCircuit()
        sleep(2)
        oldValue = self.feederSchedule.getCircuitTo()
        self.feederSchedule.tapOverflow()
        sleep(3)
        self.feederSchedule.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.feederSchedule.getCircuitTo()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditTypeAndPreset(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376013
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        # end of precondition
        self.feederSchedule.tapOverflow()
        sleep(3)
        self.feederSchedule.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuit.selectConductorType(type='CU / XHHW')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(2)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditSizeAndPreset(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376014
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        oldValue = self.feederSchedule.getCircuitSize()
        # end of precondition
        self.feederSchedule.tapOverflow()
        sleep(3)
        self.feederSchedule.tapEditCircuit()
        sleep(3)
        currentUrl = self.driver.current_url
        self.circuit.selectConductorSize(size='1/0')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(2)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.feederSchedule.getCircuitSize()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditLength(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376015
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createLargeUSCircuit()
        sleep(2)
        oldValue = self.feederSchedule.getCircuitLength()
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        newValue = self.feederSchedule.getCircuitLength()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditSIMpullHead(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376016
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createLargeUSCircuit()
        sleep(2)
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuit.toggleSIMpullHead()
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditNumberOfConductor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376019
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createLargeUSCircuit()
        sleep(2)
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuit.selectNumOfConductor(NOC='3')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Brown-Orange-Yellow')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376018
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createCircuitOfDifferentColors()
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuit.tapSelectedColorCircle(circleOrder=0)
        sleep(1)
        self.circuit.selectColorOption(color='Black')
        sleep(1)
        self.circuit.tapSelectedColorCircle(circleOrder=1)
        sleep(1)
        self.circuit.selectColorOption(color='Black')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitEditCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376017
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createLargeUSCircuit()
        sleep(2)
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapEditCircuit()
        sleep(2)
        currentUrl = self.driver.current_url
        self.circuit.tapCancel()
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
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        # end of precondition
        oldValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDeleteCircuit()
        sleep(2)
        self.feederSchedule.tapConfirmDelete()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber + 1)
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testCancelDeleteCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378729
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        oldValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        # end of precondition
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDeleteCircuit()
        sleep(2)
        self.feederSchedule.tapCancelDelete()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        sleep(3)

        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testDuplicateCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376306
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        # end of precondition
        oldValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDuplicateCircuit()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=1)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testEditDuplicatedCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376311
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDuplicateCircuit()
        sleep(2)
        # end of precondition
        oldValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapEditCircuit()
        sleep(2)
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.tapSubmit()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=1)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 1)
        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testDeleteDuplicatedCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376312
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDuplicateCircuit()
        sleep(2)
        # end of precondition
        oldValue = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDeleteCircuit()
        sleep(2)
        self.feederSchedule.tapConfirmDelete()
        sleep(2)
        newValue = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldValue, newValue + 1)

    @pytest.mark.ac
    def testDuplicateDuplicatedCircuit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1376313
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # precondition
        self.feederSchedule.tapCreateCircuit()
        self.circuit.enterRandomFrom()
        sleep(1)
        self.circuit.enterRandomTo()
        sleep(1)
        self.circuit.selectConductorType(type='CU / THHN')
        sleep(1)
        self.circuit.selectConductorSize(size='300')
        sleep(1)
        self.circuit.enterRandomLength()
        sleep(1)
        self.circuit.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuit.tapSubmit()
        sleep(3)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDuplicateCircuit()
        sleep(2)
        # end of precondition
        oldValue = self.feederSchedule.getCircuitFrom(rowOrder=0)
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDuplicateCircuit()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom(rowOrder=1)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(oldRowNumber, newRowNumber - 2)
        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testCircuitAddedToFeederSchedule(self):
        # Verify a successfully added circuit is displayed in the feeder schedule
        email = 'nick.moore+auto8@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311235
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        beforeCount = self.feederSchedule.getNumberOfRows()
        self.circuit.createCircuitWithSIMpullHead()
        sleep(1)
        afterCount = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(beforeCount + 1, afterCount)

    @pytest.mark.ac
    def testVerifyCircuitMetalOptionsUS(self):
        # Verify circuit options are correct for a US user
        email = 'nick.moore+auto9@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311227
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        USConductorList = ['CU / THHN', 'CU / XHHW', 'CU / USE', 'AL / THHN', 'AL / XHHW', 'AL / USE']
        actualConductorList = self.circuit.getConductorTypeList()

        self.assertion.assertEqual(USConductorList, actualConductorList)

    @pytest.mark.ac
    def testVerifyCircuitMetalOptionsCanada(self):
        # Verify circuit options are correct for a Canada user
        email = 'nick.moore+auto10@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311228
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        CanadaConductorList = ['CU / RW90', 'CU / RWU', 'CU / T90', 'CU / THHN', 'AL / RW90', 'AL / RWU', 'AL / T90', 'AL / THHN']
        actualConductorList = self.circuit.getConductorTypeList()

        self.assertion.assertEqual(CanadaConductorList, actualConductorList)

    @pytest.mark.ac
    def testVerifySIMpullHeadSuccessfullyAdded(self):
        # Verify that a circuit with SIMpull head is successfully added
        email = 'nick.moore+auto11@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311236
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createCircuitWithSIMpullHead()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapEditCircuit()

        self.assertion.assertEqual(self.circuit.getSIMpullHeadToggle().isOn(), True)

    @pytest.mark.ac
    def testVerifySIMpullHeadNotAdded(self):
        # Verify that a circuit with SIMpull head is not added
        email = 'nick.moore+auto12@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311237
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createGreenCircuit()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapEditCircuit()

        self.assertion.assertEqual(self.circuit.getSIMpullHeadToggle().isOn(), False)

    @pytest.mark.ac
    def testVerifySIMpullOffByDefault(self):
        # Verify that the SIMpull option is off by default
        email = 'nick.moore+auto15@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311256
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()

        self.assertion.assertEqual(self.circuit.getSIMpullHeadToggle().isOn(), False)

    @pytest.mark.ac
    def testVerifyMaxNumberOfConductorsIs6(self):
        # Verify that the max number of conductors is 6
        email = 'nick.moore+auto16@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311259
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        sizeList = ['1', '2', '3', '4', '5', '6']

        self.assertion.assertEqual(self.circuit.getConductorSizeList(), sizeList)

    @pytest.mark.ac
    def testVerifyUnitsForStandardAccount(self):
        # Verify that units are displayed in feet for standard account
        email = 'nick.moore+autostandard@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311258
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()

        self.assertion.assertEqual(self.circuit.getLength().ui_object.get_attribute('placeholder'), 'Feet')

    @pytest.mark.ac
    def testVerifyUnitsForMetricAccount(self):
        # Verify that units are displayed in meters for metric account
        email = 'nick.moore+autometric@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311257
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()

        self.assertion.assertEqual(self.circuit.getLength().ui_object.get_attribute('placeholder'), 'Meters')

    @pytest.mark.ac
    def testVerifyGreenAvailableForOneConductor(self):
        # Verify that the green color is available with one conductor selected
        email = 'nick.moore+auto17@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311254
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / THHN')
        self.circuit.selectNumOfConductor('1')
        self.circuit.selectConductorSize('4')

        self.assertion.assertExists(self.circuit.getColorOption('Green'))

    @pytest.mark.ac
    def testVerifyGreenNotAvailableForMoreThanOneConductor(self):
        # Verify that the green color is not an option when >1 conductor selected
        email = 'nick.moore+auto18@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311255
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / THHN')
        self.circuit.selectConductorSize('4')

        for i in range(2, 7, 1):
            self.circuit.selectNumOfConductor(str(i))
            self.assertion.assertNotExists(self.circuit.getColorOption('Green').ui_object)

    @pytest.mark.ac
    def testVerifyColorSwapAfterChoosingPreset(self):
        # Verify colors can be swapped out after choosing a preset
        email = 'nick.moore+auto19@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311249
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / THHN')
        self.circuit.selectConductorSize('4')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        colors = ['Yellow', 'White', 'Pink']
        for i in range(3):
            self.circuit.tapSelectedColorCircle(i)
            self.circuit.selectColorOption(colors[i])
            self.assertion.assertEqual(self.circuit.getSelectedColorCircle(i).getLabel(), colors[i])

    @pytest.mark.ac
    def testVerifyColorPresetOverridesPartialColorSelection(self):
        # Verify that when colors have been partially selected, selecting a preset updates the color selection
        email = 'nick.moore+auto21@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311250
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / THHN')
        self.circuit.selectConductorSize('4')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectColorOption('Blue')
        sleep(1)
        colorPreset = ['Brown', 'Orange', 'Yellow']
        self.circuit.selectCommonPreset('Brown-Orange-Yellow')

        for i in range(3):
            self.assertion.assertEqual(self.circuit.getSelectedColorCircle(i).getLabel(), colorPreset[i])

    @pytest.mark.ac
    def testVerifyCircuitCreatedWithOneConductorAdded(self):
        # Verify a circuit with one conductor can be created with all valid fields entered
        email = 'nick.moore+auto22@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311244
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # Create circuit with one conductor
        self.circuit.createGreenCircuitOfDifferentMetalInsulation()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapEditCircuit()

        self.assertion.assertEqual(self.circuit.getLength().getValue(), '100')
        self.assertion.assertEqual(self.circuit.getSIMpullHeadToggle().isOn(), False)
        self.assertion.assertEqual(self.circuit.getSelectedColorCircle(0).getLabel(), 'Green')
        self.assertion.assertEqual(self.circuit.getNumOfConductorPicker().getValue(), '1')

    @pytest.mark.ac
    def testVerifyCircuitCreatedWithMoreThanOneConductorAdded(self):
        # Verify a circuit with >1 conductor can be created with all valid fields entered
        email = 'nick.moore+auto23@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311245
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        # Create circuit with 4 conductors
        self.circuit.createLargeCACircuit()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapEditCircuit()

        self.assertion.assertEqual(self.circuit.getLength().getValue(), '500')
        self.assertion.assertEqual(self.circuit.getSIMpullHeadToggle().isOn(), False)
        self.assertion.assertEqual(self.circuit.getNumOfConductorPicker().getValue(), '4')
        for i in range(4):
            self.assertion.assertEqual(self.circuit.getSelectedColorCircle(i).getLabel(), 'Black')

    @pytest.mark.ac
    def testVerifyChangeNumConductorsResetsColorSelection(self):
        # Verify when colors have been selected, changing the number of conductors resets the color selection
        email = 'nick.moore+auto24@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311247
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / THHN')
        self.circuit.selectConductorSize('4')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        sleep(1)
        self.circuit.selectNumOfConductor('1')

        self.assertion.assertEqual(unidecode.unidecode(self.circuit.getSelectedColorCircle(0).getLabel()), '--')

    @pytest.mark.ac
    def testVerifyPresetColorSelectionOverridesAnotherPreset(self):
        # Verify when a color preset has been selected, selecting another preset overrides the color selection
        email = 'nick.moore+auto25@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311248
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('4')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        sleep(1)
        self.circuit.selectCommonPreset('Black-Black-Black')

        for i in range(3):
            self.assertion.assertEqual(self.circuit.getSelectedColorCircle(i).getLabel(), 'Black')

    @pytest.mark.ac
    def testVerifyConductorSizeResetsAfterChangingMetalType(self):
        # Verify when a size is not available, changing metal/insulation type resets the size selection
        email = 'nick.moore+auto26@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311251
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('4')
        sleep(1)
        self.circuit.selectConductorType('CU / THHN')
        if self.isSafari:
            sizeLabel = 'Select Size1'
        else:
            sizeLabel = 'Select Size\n1'

        self.assertion.assertEqual(unidecode.unidecode(self.circuit.getConductorSizePicker().getLabel()), sizeLabel)

    @pytest.mark.ac
    def testVerifyChangingMetalResetsColorSelection(self):
        # Verify when colors are selected, changing metal resets the color selection
        email = 'nick.moore+auto27@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311252
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / THHN')
        self.circuit.selectConductorSize('4')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        sleep(1)
        self.circuit.selectConductorType('CU / XHHW')

        for i in range(3):
            self.assertion.assertEqual(unidecode.unidecode(self.circuit.getSelectedColorCircle(i).getLabel()), '--')

    @pytest.mark.ac
    def testVerifyChangingSizeResetsColorSelection(self):
        # Verify when colors are selected, changing size resets the color selection
        email = 'nick.moore+auto28@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1311253
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapCreateCircuit()
        self.circuit.selectConductorType('CU / THHN')
        self.circuit.selectConductorSize('4')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        sleep(1)
        self.circuit.selectConductorSize('1')

        for i in range(3):
            self.assertion.assertEqual(unidecode.unidecode(self.circuit.getSelectedColorCircle(i).getLabel()), '--')