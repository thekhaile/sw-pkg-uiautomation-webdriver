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



class TestEditJobSettings(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestEditJobSettings, self).__init__(*args, **kwargs)
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
    def testEditJobNameWithNewName(self):
        # Verify that the modified job with unique name can be saved on Create New Job page
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

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
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

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
        expectedErrorMsg = 'Job name already exists.'
        actualErrorMsg = self.job.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.job.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testEditSIMPullReel(self):
        # Verify when a SIMpull Reel selection is changed for the job, that the new setting is updated in the database
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

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
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

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
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

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
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

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
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

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
    def testEditedHeightIsSaved(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1302120
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.project.createAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        oldValue = self.job.getHeight()
        sleep(2)
        self.job.enterHeight('888')
        sleep(1)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        newValue = self.job.getHeight()
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testEditedWidthIsSaved(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1302107
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.project.createAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        oldValue = self.job.getWidth()
        sleep(2)
        self.job.enterWidth('888')
        sleep(1)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        newValue = self.job.getWidth()
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testEditedWeightIsSaved(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1302133
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.project.createAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        oldValue = self.job.getWeight()
        sleep(2)
        self.job.enterWeight('888')
        sleep(1)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        newValue = self.job.getWeight()
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testExitEditJobSettingsTansitionsToViewJobSummaryScreen(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1302149
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.project.createAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        oldUrl = self.driver.current_url
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        self.job.tapCancel()
        sleep(2)
        newUrl = self.driver.current_url
        self.assertion.assertEqual(oldUrl, newUrl)