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

    # Test SCR-104 Create New Job

    @pytest.mark.ac
    def testCreateJobWithUniqueNameAndToggleOn(self):
        # Verify that a new job with unique name can be created on Create New Job page and Toggle On
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301968
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        jobName = self.jobs.generateRandomName()
        self.jobs.enterJobName(jobName)
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(1)
        self.jobs.enterHeight('999')
        sleep(1)
        self.jobs.enterWidth('66')
        sleep(1)
        self.jobs.toggleSIMpullReel()
        sleep(1)
        self.assertion.assertTrue(self.jobs.getSIMpullReelToggle().isOn(), 'Toggle has the off state after being tapped')
        self.jobs.tapSubmit()
        sleep(1)
        viewJobName = self.jobs.getJobName(rowOrder=0)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)
        self.assertion.assertEqual(jobName, viewJobName)

    @pytest.mark.ac
    def testCreateJobWithUniqueNameAndToggleOff(self):
        # Verify that a new job with unique name can be created on Create New Job page and Toggle Off
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301974
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        jobName = self.jobs.generateRandomName()
        self.jobs.enterJobName(jobName)
        self.jobs.enterWeight('99')
        sleep(1)
        self.jobs.tapSubmit()
        sleep(1)
        viewJobName = self.jobs.getJobName(rowOrder=0)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)
        self.assertion.assertEqual(jobName, viewJobName)

    @pytest.mark.ac
    def testCreateJobWithoutUniqueName(self):
        # Verify when entering a same name for a new job, that an alert is displayed on the Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301969
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        # Preconditions: Set up an existing job
        self.jobs.tapCreateJob()
        sleep(1)
        name = self.jobs.generateRandomName()
        self.jobs.enterJobName(name)
        sleep(1)
        self.jobs.tapSubmit()
        sleep(1)
        # End of preconditions
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName(name)
        self.jobs.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Job name already exists'
        actualErrorMsg = self.jobs.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.jobs.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateJobWithOver30CharLimit(self):
        # Verify that when entering more than 30 char for job name, that an alert is displayed on the Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301994
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('abc def ghi jkl mno pqrs tuv w1')
        sleep(1)
        self.jobs.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Project Name cannot exceed 30 characters.'
        actualErrorMsg = self.jobs.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.jobs.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testExitCreateJobProcess(self):
        # Verify that by clicking/tapping Cancel button exit the Create New Job page at any time
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301979
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

    @pytest.mark.ac
    def testEditJobNameWithNewName(self):
        # Verify that the modified job with unique name can be saved on Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302074
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        jobName = self.jobs.generateRandomName()
        self.jobs.enterJobName(jobName)
        self.jobs.tapSubmit()
        sleep(2)
        viewJobName = self.jobs.getJobName(rowOrder=0)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)
        self.assertion.assertEqual(jobName, viewJobName)

    @pytest.mark.ac
    def testEditJobNameWithSameName(self):
        # Verify when entering a same name for a modified job, that an alert is displayed on the Edit Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302075
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        self.jobs.enterRandomJobName()
        self.jobs.tapSubmit()
        # Get the job name of the second row
        name = self.jobs.getJobName(rowOrder=1)
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName(name)
        sleep(1)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Job name already exists'
        actualErrorMsg = self.jobs.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.jobs.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testEditSIMPullReel(self):
        # Verify when a SIMpull Reel selection is changed for the job, that the new setting is updated in the database
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302082
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

    @pytest.mark.ac
    def testExitEditSettings(self):
        # Verify that by clicking/tapping Cancel button exit the Edit Job Settings page at any time
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302086
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

    @pytest.mark.ac
    def testEditHeightAndWidth(self):
        # Verify that the modified width, height and weight restriction field can be saved on Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302080
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

    @pytest.mark.ac
    def testEditWeightAndHeight(self):
        # Verify that the modified width, height and weight restriction field can be saved on Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302078
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
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testEditWeightAndWidth(self):
        # Verify that the modified width, height and weight restriction field can be saved on Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302079
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
        self.jobs.enterWidth('888')
        sleep(1)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testDeleteInProgressJob(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1379235
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        jobName = self.jobs.getJobName(rowOrder=0)
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapDeleteJob()
        sleep(2)
        self.jobs.tapConfirmDelete()
        sleep(2)
        newJobName = self.jobs.getJobName(rowOrder=0)

        self.assertion.assertNotEqual(jobName, newJobName)

    @pytest.mark.ac
    def testCancelDeleteInProgressJob(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1379242
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        jobName = self.jobs.getJobName(rowOrder=0)
        self.jobs.tapOverflow()
        sleep(2)
        self.jobs.tapDeleteJob()
        sleep(2)
        self.jobs.tapCancelDelete()
        sleep(3)
        newJobName = self.jobs.getJobName(rowOrder=0)

        self.assertion.assertEqual(jobName, newJobName)