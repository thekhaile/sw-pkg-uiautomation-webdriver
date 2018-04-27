from time import sleep
import pytest
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.project import Project
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components.requestQuote import RequestQuote
from southwire_pkg_uiautomation_webdriver.components.jobSummary.reels import Reels



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
        self.project = Project(self)
        self.circuit = Circuit(self)
        self.requestQuote = RequestQuote(self)
        self.reels = Reels(self)

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

    @pytest.mark.ac
    def testCreateJobWithoutInputtingWidthField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301971
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
    def testCreateJobWithoutInputtingHeightField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301972
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
    def testCreateJobWithoutInputtingWeightField(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301973
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        sleep(1)
        self.job.enterHeight('999')
        sleep(1)
        self.job.enterWidth('66')
        sleep(1)
        self.job.toggleSIMpullReel()
        sleep(1)
        self.assertion.assertTrue(self.job.getSIMpullReelToggle().isOn(),
                                  'Toggle has the off state after being tapped')
        self.job.tapSubmit()
        sleep(1)
        viewJobName = self.jobList.getJobName(rowOrder=0)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)
        self.assertion.assertEqual(jobName, viewJobName)

    @pytest.mark.ac
    def testNewJobIsListedOnTheJobList(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1301977
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.project.createAProject()
        self.jobList.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        sleep(1)
        self.job.tapSubmit()
        sleep(1)
        viewJobName = self.jobList.getJobName(rowOrder=0)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)
        self.assertion.assertEqual(jobName, viewJobName)
