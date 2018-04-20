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
from southwire_pkg_uiautomation_webdriver.components.jobSummary.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.jobSummary.reels import Reels


class TestViewJobSummary(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestViewJobSummary, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)
        self.reels = Reels(self)

    @pytest.mark.ac
    def testJobTitleIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393651
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getJobNameOnViewJobSummary()
        self.assertion.assertEqual(el, '1')

    @pytest.mark.ac
    def testDateCreatedIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393652
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getDateCreated()
        self.assertion.assertEqual(el, '4/20/2018')

    @pytest.mark.ac
    def testDateModifiedIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393653
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getDateCreated()
        self.assertion.assertEqual(el, '4/20/2018')

    @pytest.mark.ac
    def testDateSentForRFQIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393654
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getQuoteSubmittedDate()
        self.assertion.assertEqual(el, '4/20/18')

    @pytest.mark.ac
    def testFromIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393655
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitFrom()
        self.assertion.assertEqual(el, 'a')

    @pytest.mark.ac
    def testToIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393656
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitTo()
        self.assertion.assertEqual(el, 'b')

    @pytest.mark.ac
    def testSizeIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393657
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitSize()
        self.assertion.assertEqual(el, '1')

    @pytest.mark.ac
    def testLengthIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393658
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitLength()
        self.assertion.assertEqual(el, "123'")

    @pytest.mark.ac1
    def testReelIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393662
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitReelName()
        self.assertion.assertEqual(el, 'reel 1')
