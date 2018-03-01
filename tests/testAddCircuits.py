import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects
from southwire_pkg_uiautomation_webdriver.components.jobs import Jobs
from southwire_pkg_uiautomation_webdriver.components.addCircuits import AddCircuits

class TestJobs(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestJobs, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)
        self.jobs = Jobs(self)
        self.addCircuits = AddCircuits(self)

    # TEST SCR-28 Add Circuit to Feeder Schedule

    def testCreateCircuitWithOnlyRequiredFieldsForUS(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)


    def testCreateCircuitWithOnlyRequiredFieldsForCanada(self):
        email = 'jess.moss@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testCeateCircuitWithAllFields(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.toggleSIMpullHead()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    def testExitAddCircuitProcess(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.tapCancel()
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Error Msg
    def testSIMpullHeadIsNotAvailableForSizes6Conductors(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize(size='6')
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.jobs.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)

        self.assertion.assertNotEqual(currentUrl, newUrl)

        el = self.addCircuits.getSIMpullHeadToggle()
        self.assertion.assertFalse(el.isEnabled())

    def testSIMpullHeadIsNotAvailableForSizes8Conductors(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize(size='6')
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Some Error'
        actualErrorMsg = self.jobs.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)

        self.assertion.assertNotEqual(currentUrl, newUrl)

        el = self.addCircuits.getSIMpullHeadToggle()
        self.assertion.assertFalse(el.isEnabled())

    # Missing Required Fields
    def testCreateCircuitWithoutFrom(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.addCircuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    def testCreateCircuitWithoutTo(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.addCircuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    def testCreateCircuitWithoutType(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.addCircuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    def testCreateCircuitWithoutSize(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.addCircuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    def testCreateCircuitWithoutLength(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.addCircuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    def testCreateCircuitWithoutNOC(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectConductorColor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.addCircuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    def testCreateCircuitWithoutColor(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        self.jobs.tapConfigureJob()
        self.jobs.tapAddCircuit()
        currentUrl = self.driver.current_url
        self.addCircuits.enterFrom()
        sleep(1)
        self.addCircuits.enterTo()
        sleep(1)
        self.addCircuits.selectConductorType()
        sleep(1)
        self.addCircuits.selectConductorSize()
        sleep(1)
        self.addCircuits.enterCircuitLength()
        sleep(1)
        self.addCircuits.selectNumOfConductor()
        sleep(1)
        self.addCircuits.tapSubmit()
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.addCircuits.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())
