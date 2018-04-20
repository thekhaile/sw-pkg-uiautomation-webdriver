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


class TestJobList(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestJobList, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)

    @pytest.mark.ac
    def testVerifyJobListCount(self):
        # Verify that all jobs are listed on the jobs list page
        email = 'nick.moore+autojoblist@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302167
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        actualJobCount = self.jobList.getJobCount()

        self.assertion.assertEqual(3, actualJobCount)

    @pytest.mark.ac
    def testVerifyJobNamesOnJobList(self):
        # Verify that job names are correct for each job on the job list
        email = 'nick.moore+autojoblist@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302168
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.assertion.assertEqual('Job3', self.jobList.getJobName(rowOrder=0))
        self.assertion.assertEqual('Job2', self.jobList.getJobName(rowOrder=1))
        self.assertion.assertEqual('Job1', self.jobList.getJobName(rowOrder=2))

    @pytest.mark.ac
    def testVerifyDateCreatedOnJobList(self):
        # Verify that Date Created is displayed for each job in the job list
        email = 'nick.moore+autojoblist@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302169
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()

        for i in range(3):
            self.assertion.assertEqual(self.jobList.getJobCreatedDate(i), '4/20/2018')

    @pytest.mark.ac
    def testVerifyNumberOfCircuitsOnJobList(self):
        # Verify the number of circuits is displayed for each job in the job list
        email = 'nick.moore+autojoblist@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302170
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()

        self.assertion.assertEqual('0', self.jobList.getNumberOfCircuits(0))
        self.assertion.assertEqual('1', self.jobList.getNumberOfCircuits(1))
        self.assertion.assertEqual('2', self.jobList.getNumberOfCircuits(2))

    @pytest.mark.ac
    def testVerifyNumberOfReelsOnJobList(self):
        # Verify the number of reels is displayed for each job in the job list
        email = 'nick.moore+autojoblist@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302171
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()

        self.assertion.assertEqual('0', self.jobList.getNumberOfReels(0))
        self.assertion.assertEqual('1', self.jobList.getNumberOfReels(1))
        self.assertion.assertEqual('2', self.jobList.getNumberOfReels(2))

    @pytest.mark.ac1
    def testVerifyRecentJobListPosition(self):
        # Verify the most recent created job is at the top of the job list
        email = 'nick.moore+autojoblist@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1302172
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        recentJobName = self.jobList.getJobName()

        self.assertion.assertEqual('Job3', recentJobName)