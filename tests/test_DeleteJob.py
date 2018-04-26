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



class TestDeleteJob(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestDeleteJob, self).__init__(*args, **kwargs)
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

    def testDeleteOptionIsAvailableForInProgressJob(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1379231
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """Precondition"""
        self.jobList.tapCreateJob()
        sleep(1)
        name = self.job.generateRandomName()
        self.job.enterJobName(name)
        sleep(1)
        self.job.tapSubmit()
        sleep(1)
        """End of Precondition"""
        self.jobList.tapOverflow()

        self.assertion.assertExists(self.jobList.getDeleteJobButton().ui_object)

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
    def testJobCountDecreasesBy1AfterASuccessfulDelete(self):
        email = 'khai.le+SW1@mutualmobile.com'
        password = 'password'

        self.caseId = 1396903
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """Precondition"""
        self.job.createAJob()
        """End of Precondition"""
        self.navigation.navigateToProjectsPage()
        sleep(2)
        oldCount = self.projectList.getProjectJobCount()
        self.projectList.selectAProject()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDeleteJob()
        self.jobList.tapConfirmDelete()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        newCount = self.projectList.getProjectJobCount()

        self.assertion.assertEqual(int(oldCount)-1, int(newCount))
