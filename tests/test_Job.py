from time import sleep
import pytest
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary


class TestJob(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestJob, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)

    """Create job"""
    @pytest.mark.ac
    def testCreateJobWithUniqueNameAndToggleOn(self):
        # Verify that a new job with unique name can be created on Create New Job page and Toggle On
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301968
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        sleep(1)
        self.job.enterWeight('88')
        sleep(1)
        self.job.enterHeight('999')
        sleep(1)
        self.job.enterWidth('66')
        sleep(1)
        self.job.toggleSIMpullReel()
        sleep(1)
        self.assertion.assertTrue(self.job.getSIMpullReelToggle().isOn(), 'Toggle has the off state after being tapped')
        self.job.tapSubmit()
        sleep(1)
        viewJobName = self.jobList.getJobName(rowOrder=0)
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
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        self.job.enterWeight('99')
        sleep(1)
        self.job.tapSubmit()
        sleep(1)
        viewJobName = self.jobList.getJobName(rowOrder=0)
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
        self.projectList.selectAProject()
        # Preconditions: Set up an existing job
        self.jobList.tapCreateJob()
        sleep(1)
        name = self.job.generateRandomName()
        self.job.enterJobName(name)
        sleep(1)
        self.job.tapSubmit()
        sleep(1)
        # End of preconditions
        self.jobList.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.job.enterJobName(name)
        self.job.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Job name already exists.'
        actualErrorMsg = self.job.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.job.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateJobWithOver30CharLimit(self):
        # Verify that when entering more than 30 char for job name, that an alert is displayed on the Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301994
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.job.enterJobName('abc def ghi jkl mno pqrs tuv w1')
        sleep(1)
        self.job.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Job name cannot exceed 30 characters.'
        actualErrorMsg = self.job.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.job.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testExitCreateJobProcess(self):
        # Verify that by clicking/tapping Cancel button exit the Create New Job page at any time
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301979
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.job.enterRandomJobName()
        sleep(1)
        self.job.enterWeight('88')
        sleep(1)
        self.job.tapCancel()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    """Edit job settings"""

    @pytest.mark.ac
    def testEditJobNameWithNewName(self):
        # Verify that the modified job with unique name can be saved on Create New Job page
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302074
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        self.job.tapSubmit()
        sleep(2)
        viewJobName = self.jobList.getJobName(rowOrder=0)
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
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterRandomJobName()
        self.job.tapSubmit()
        # Get the job name of the second row
        name = self.jobList.getJobName(rowOrder=1)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.job.enterJobName(name)
        sleep(1)
        self.job.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Job name already exists'
        actualErrorMsg = self.job.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.job.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testEditSIMPullReel(self):
        # Verify when a SIMpull Reel selection is changed for the job, that the new setting is updated in the database
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302082
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.job.toggleSIMpullReel()
        sleep(1)
        self.job.tapSubmit()
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
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.job.enterRandomJobName()
        sleep(1)
        self.job.toggleSIMpullReel()
        sleep(1)
        self.job.tapCancel()
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
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.job.enterHeight('888')
        sleep(1)
        self.job.enterWidth('888')
        sleep(1)
        self.job.tapSubmit()
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
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.job.enterWeight('888')
        sleep(1)
        self.job.enterHeight('888')
        sleep(1)
        self.job.tapSubmit()
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
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        currentUrl = self.driver.current_url
        self.job.enterWeight('888')
        sleep(1)
        self.job.enterWidth('888')
        sleep(1)
        self.job.tapSubmit()
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
        self.projectList.selectAProject()
        # precondition
        self.jobList.tapCreateJob()
        sleep(1)
        name = self.job.generateRandomName()
        self.job.enterJobName(name)
        sleep(1)
        self.job.tapSubmit()
        sleep(1)
        # end of precondition
        oldJobCount = self.jobList.getJobCount()
        jobName = self.jobList.getJobName(rowOrder=0)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDeleteJob()
        sleep(2)
        self.jobList.tapConfirmDelete()
        sleep(2)
        newJobCount = self.jobList.getJobCount()
        self.assertEqual(oldJobCount-1, newJobCount)
        if newJobCount >= 1:
            newJobName = self.jobList.getJobName(rowOrder=0)
            self.assertion.assertNotEqual(jobName, newJobName)

    @pytest.mark.ac
    def testCancelDeleteInProgressJob(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1379242
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        jobName = self.jobList.getJobName(rowOrder=0)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDeleteJob()
        sleep(2)
        self.jobList.tapCancelDelete()
        sleep(3)
        newJobName = self.jobList.getJobName(rowOrder=0)

        self.assertion.assertEqual(jobName, newJobName)

    @pytest.mark.ac
    def testDuplicatedJobSettings(self):
        # Verify the duplicated job's settings are identical to the original
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388781
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterJobName(self.job.generateRandomName())
        self.job.enterHeight("1000")
        self.job.enterWidth("1000")
        self.job.enterWeight("1000")
        simpullToggle = self.job.getSIMpullReelToggle().getValue()
        self.job.tapSubmit()
        sleep(1)
        self.jobList.selectAJob()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        self.jobList.selectAJob()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapEditSettings()
        sleep(1)
        height = self.job.getHeight()
        width = self.job.getWidth()
        weight = self.job.getWeight()

        self.assertion.assertEqual('1000', height)
        self.assertion.assertEqual('1000', width)
        self.assertion.assertEqual('1000', weight)
        self.assertion.assertEqual(simpullToggle, self.job.getSIMpullReelToggle().getValue())

    @pytest.mark.ac
    def testDuplicatedJobReels(self):
        # Verify the duplicated job's reels are identical to the original
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388785
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        sleep(1)
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        for i in range(2):
            self.reelList.tapCreateReel()
            self.reel.enterRandomReelName()
            self.reel.tapSubmit()
        reelList = self.reelList.getReels()
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        sleep(1)
        self.jobList.selectAJob()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        newReelList = self.reelList.getReels()

        self.assertion.assertEqual(reelList, newReelList)

    @pytest.mark.ac
    def testDuplicatedJobCount(self):
        # Verify the list of jobs is incremented after duplication
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388791
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterRandomJobName()
        self.job.tapSubmit()
        sleep(1)
        jobCount = self.jobList.getJobCount()
        sleep(1)
        self.jobList.selectAJob()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        newJobCount = self.jobList.getJobCount()

        self.assertion.assertEqual(jobCount + 1, newJobCount)

    @pytest.mark.ac
    def testDuplicatedJobListPosition(self):
        # Verify the duplicated job is placed at the top of the job list
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388790
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        sleep(1)
        self.jobList.selectAJob()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        newJobName = self.job.generateRandomName()
        self.job.enterJobName(newJobName)
        self.job.tapSubmit()
        sleep(1)
        recentJobName = self.jobList.getJobName(rowOrder=0)

        self.assertion.assertEqual(newJobName, recentJobName)

    @pytest.mark.ac
    def testDuplicatedJobWithNonUniqueName(self):
        # Verify when a non-unique job name is added that an error appears
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388773
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        self.job.tapSubmit()
        sleep(1)
        self.jobList.selectAJob()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(jobName)
        self.job.tapSubmit()
        expectedErrorMsg = 'Job name already exists.'
        actualErrorMsg = self.job.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)