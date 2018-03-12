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
        self.circuits.selectConductorType(type='CU|THHN')
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

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateCircuitWithOnlyRequiredFieldsForCanada(self):
        email = 'jess.moss@mutualmobile.com'
        password = 'password'

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
        self.circuits.selectConductorType(type='CU|RW90')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Black-Black-Black-Black')
        sleep(1)
        self.circuits.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateCircuitWithAllFields(self):
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
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU|THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
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

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitAddCircuitProcess(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        sleep(3)
        self.feederSchedule.tapCreateCircuit()
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.tapCancel()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Error Msg
    # @pytest.mark.ac5
    # def testSIMpullHeadIsNotAvailableForSizes6Conductors(self):
    #     email = 'ningxin.liao@mutualmobile.com'
    #     password = 'newpassword'
    #
    #     self.navigation.navigateToLoginPage()
    #     self.authentication.login(email, password)
    #     self.projects.selectAProject()
    #     self.jobs.selectAJob()
    #     sleep(3)
    #     self.jobs.tapConfigureJob()
    #     sleep(3)
    #     self.feederSchedule.tapCreateCircuit()
    #     currentUrl = self.driver.current_url
    #     self.circuits.enterFrom('ABC123')
    #     sleep(1)
    #     self.circuits.enterTo('QWE098')
    #     sleep(1)
    #     self.circuits.selectConductorType(type='CU|THHN')
    #     sleep(1)
    #     self.circuits.selectConductorSize(size='6')
    #     sleep(1)
    #     self.circuits.enterCircuitLength('123')
    #     sleep(1)
    #     self.circuits.toggleSIMpullHead()
    #     sleep(1)
    #     self.circuits.selectNumOfConductor(NOC='4')
    #     sleep(1)
    #     self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
    #     sleep(1)
    #     self.circuits.tapSubmit()
    #     sleep(3)
    #     newUrl = self.driver.current_url
    #     expectedErrorMsg = " ERROR MSG "
    #     actualErrorMsg = self.jobs.getErrorMsg()
    #
    #     self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
    #
    #     self.assertion.assertNotEqual(currentUrl, newUrl)
    #
    #     el = self.circuits.getSIMpullHeadToggle()
    #     self.assertion.assertFalse(el.isEnabled())
    #
    # @pytest.mark.ac6
    # def testSIMpullHeadIsNotAvailableForSizes8Conductors(self):
    #     email = 'ningxin.liao@mutualmobile.com'
    #     password = 'newpassword'
    #
    #     self.navigation.navigateToLoginPage()
    #     self.authentication.login(email, password)
    #     self.projects.selectAProject()
    #     self.jobs.selectAJob()
    #     sleep(3)
    #     self.jobs.tapConfigureJob()
    #     sleep(3)
    #     self.feederSchedule.tapCreateCircuit()
    #     currentUrl = self.driver.current_url
    #     self.circuits.enterFrom('ABC123')
    #     sleep(1)
    #     self.circuits.enterTo('QWE098')
    #     sleep(1)
    #     self.circuits.selectConductorType(type='CU|THHN')
    #     sleep(1)
    #     self.circuits.selectConductorSize(size='8')
    #     sleep(1)
    #     self.circuits.enterCircuitLength('123')
    #     sleep(1)
    #     self.circuits.toggleSIMpullHead()
    #     sleep(1)
    #     self.circuits.selectNumOfConductor(NOC='4')
    #     sleep(1)
    #     self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
    #     sleep(1)
    #     self.circuits.tapSubmit()
    #     sleep(3)
    #     newUrl = self.driver.current_url
    #     expectedErrorMsg = " ERROR MSG "
    #     actualErrorMsg = self.jobs.getErrorMsg()
    #
    #     self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
    #
    #     self.assertion.assertNotEqual(currentUrl, newUrl)
    #
    #     el = self.circuits.getSIMpullHeadToggle()
    #     self.assertion.assertFalse(el.isEnabled())

    # Missing Required Fields
    @pytest.mark.ac
    def testCreateCircuitWithoutFrom(self):
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
        currentUrl = self.driver.current_url
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU|THHN')
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
        self.circuits.selectConductorType(type='CU|THHN')
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

    @pytest.mark.ac9
    def testCreateCircuitWithoutType(self):
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
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)

        el = self.circuits.getConductorSizePicker()




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

    @pytest.mark.ac10
    def testCreateCircuitWithoutSize(self):
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
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU|THHN')
        sleep(1)
        self.circuits.enterCircuitLength('123')
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

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.circuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateCircuitWithoutLength(self):
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
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU|THHN')
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

    @pytest.mark.ac12
    def testCreateCircuitWithoutNOC(self):
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
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU|THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.enterCircuitLength('123')
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
    def testCreateCircuitWithoutColor(self):
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
        currentUrl = self.driver.current_url
        self.circuits.enterFrom('ABC123')
        sleep(1)
        self.circuits.enterTo('QWE098')
        sleep(1)
        self.circuits.selectConductorType(type='CU|THHN')
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

    #test functionality eg. change color
    @pytest.mark.func
    def testSwapColor(self):
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
        sleep(3)
        self.circuits.selectConductorType(type='CU|THHN')
        sleep(1)
        self.circuits.selectConductorSize(size='300')
        sleep(1)
        self.circuits.selectNumOfConductor(NOC='4')
        sleep(1)
        self.circuits.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.circuits.tapSelectedColorCircle(circleOrder=0)
        sleep(1)
        self.circuits.selectColorOption(color='Black')
        sleep(3)

