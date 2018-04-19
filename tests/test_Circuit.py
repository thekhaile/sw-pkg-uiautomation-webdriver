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


class TestCircuits(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestCircuits, self).__init__(*args, **kwargs)
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
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
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
        expectedErrorMsg = 'Heads cannot be applied to size 6 or 8.'
        actualErrorMsg = self.circuit.getErrorMsg()

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



