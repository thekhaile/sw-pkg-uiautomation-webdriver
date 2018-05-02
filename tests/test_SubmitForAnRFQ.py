import pytest
from time import sleep
import unidecode
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.requestQuote import RequestQuote
from southwire_pkg_uiautomation_webdriver.components.registration import Registration

class TestSubmitForAnRFQ(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestSubmitForAnRFQ, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.jobList = JobList(self)
        self.jobSummary = JobSummary(self)
        self.job = Job(self)
        self.circuit = Circuit(self)
        self.reel = Reel(self)
        self.feederSchedule = FeederSchedule(self)
        self.reelList = ReelList(self)
        self.requestQuote = RequestQuote(self)
        self.registration = Registration(self)

    @pytest.mark.ac
    def testSubmitRFQForInProgressJob(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1301710
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(),'In progress job is submitted for RFQ')

    @pytest.mark.ac
    def testSubmitRFQForInvalidJob(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391887
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        msg = unidecode.unidecode(self.requestQuote.getErrorMessage())
        self.assertion.assertEqual(msg, "You don't have any reels to submit a quote request.")

    @pytest.mark.ac
    def testSouthwireEmployeeCanSubmitRFQ(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391892
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.selectContactRole(role='Southwire Employee')
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(), 'In progress job is submitted for RFQ')