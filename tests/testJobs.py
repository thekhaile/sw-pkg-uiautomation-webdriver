import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects
from southwire_pkg_uiautomation_webdriver.components.jobs import Jobs

class TestJobs(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestJobs, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)
        self.jobs = Jobs(self)

    @pytest.mark.sandbox
    def testCreateAJob(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('Test Job Name 123')
        sleep(2)
        self.jobs.enterWeight('5000')
        sleep(2)
        self.jobs.enterWidth('50')
        sleep(2)
        self.jobs.toggleSIMpullReel()
        sleep(2)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

    # Test SCR-104 Create New Job
    # Verify that a new job with unique name can be created on Create New Job page and Toggle On
    @pytest.mark.ac
    def testCreateJobWithUniqueNameAndToggleOn(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterRandomJobName()
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(1)
        self.jobs.enterHeight('999')
        sleep(1)
        self.jobs.enterWidth('66')
        sleep(1)
        self.jobs.toggleSIMpullReel()
        sleep(1)
        self.jobs.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Verify that a new job with unique name can be created on Create New Job page and Toggle Off
    @pytest.mark.ac
    def testCreateJobWithUniqueNameAndToggleOff(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterRandomJobName()
        sleep(1)
        self.jobs.enterWeight('99')
        sleep(1)
        self.jobs.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Verify when entering a same name for a new job, that an alert is displayed on the Create New Job page
    @pytest.mark.ac
    def testCreateJobWithoutUniqueName(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('Ningxin 1st Job')
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(1)
        self.jobs.toggleSIMpullReel()
        sleep(1)
        self.jobs.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Job name already exists'
        actualErrorMsg = self.jobs.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

    # Verify that when entering more than 30 char for job name, that an alert is displayed on the Create New Job page
    @pytest.mark.ac
    def testCreateJobWithOver30CharLimit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('abc def ghi jkl mno pqrs tuv w1')
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(1)
        self.jobs.enterHeight('999')
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Project Name cannot exceed 30 characters.'
        actualErrorMsg = self.jobs.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)


    # Verify that by clicking/tapping Cancel button exit the Create New Job page at any time
    @pytest.mark.ac
    def testExitCreateJobProcess(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterRandomJobName()
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(1)
        self.jobs.tapCancel()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Test SCR-105 Edit Job Settings
    # Verify that the modified job with unique name can be saved on Create New Job page
    @pytest.mark.ac
    def testEditJobNameWithNewName(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.enterRandomJobName()
        sleep(1)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Verify when entering a same name for a modified job, that an alert is displayed on the Edit Job page
    @pytest.mark.ac
    def testEditJobNameWithNewName(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.enterRandomJobName()
        sleep(1)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

    # Verify when a SIMpull Reel selection is changed for the job, that the new setting is updated in the database
    @pytest.mark.ac
    def testEditWeightHeightAndWidth(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.toggleSIMpullReel()
        sleep(1)
        self.jobs.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Verify that by clicking/tapping Cancel button exit the Edit Job Settings page at any timeVerify that by clicking
    # Cancel button exit the Edit Job Settings page at any time
    @pytest.mark.ac
    def testEditWeightHeightAndWidth(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.enterRandomJobName()
        sleep(1)
        self.jobs.toggleSIMpullReel()
        sleep(1)
        self.jobs.tapCancel()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Verify that the modified width, height and weight restriction field can be saved on Create New Job page
    @pytest.mark.ac
    def testEditWeightHeightAndWidth(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.enterWeight('888')
        sleep(1)
        self.jobs.enterHeight('888')
        sleep(1)
        self.jobs.enterWidth('888')
        sleep(1)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)