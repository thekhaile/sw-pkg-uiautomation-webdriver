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

        self.caseId = 1391886
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(),'Verify in progress job is submitted for RFQ')

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
        self.registration.tapSubmit()
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(), 'Verify Job is submitted for RFQ')

    @pytest.mark.ac
    def testDistributorCanSubmitRFQ(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391893
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.selectContactRole(role='Distributor')
        self.registration.tapSubmit()
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(), 'Verify Job is submitted for RFQ')

    @pytest.mark.ac
    def testContractorCanSubmitRFQ(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391894
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.selectContactRole(role='Contractor')
        self.registration.tapSubmit()
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(), 'Verify Job is submitted for RFQ')

    @pytest.mark.ac
    def testSaleAgentCanSubmitRFQ(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391895
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.registration.tapAccount()
        sleep(2)
        self.registration.selectContactRole(role='Sales/Agent')
        self.registration.tapSubmit()
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(), 'Verify Job is submitted for RFQ')

    @pytest.mark.ac
    def testCannotSubmitRFQWhenNoReel(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391902
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
    def testCannotSubmitRFQWhenHaveUnassignedCircuit(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391904
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        msg = unidecode.unidecode(self.requestQuote.getErrorMessage())
        self.assertion.assertEqual(msg, "Assign all circuits to a reel to submit a quote request.")

    @pytest.mark.ac
    def testCannotSubmitRFQWhenHaveSIMpullReel(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391906
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
        self.reel.createSIMpullReelWithNoRestriction()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        msg = unidecode.unidecode(self.requestQuote.getErrorMessage())
        self.assertion.assertEqual(msg, "Quotes with SIMpull (tm) reels must be submitted through your SIMpull (tm) Partner Distributor.")

    @pytest.mark.ac
    def testJobStatusIsUpdatedOnViewJobSummary(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391919
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(), 'Verify job status is updated')

    @pytest.mark.ac
    def testRFQStatusIsUpdated(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391920
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.navigation.tapJobBreadcrumb()
        sleep(2)
        self.assertion.assertExists(self.requestQuote.getQuoteSubmitted(), 'Verify quote submitted is displayed')

    @pytest.mark.ac
    def testJobSubmissionDateIsDisplayed(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391921
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate(), 'Verify job submission date is displayed')

    @pytest.mark.ac
    def testEmailCanBeEnteredOnRequestForQuote(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391931
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.enterEmail('ningxin.liao@mutualmobile.com')
        sleep(2)
        self.assertion.assertExists(self.requestQuote.getEmail().getLabel(), 'Verify email is displayed')
        self.requestQuote.tapSubmit()

    @pytest.mark.ac
    def testJobSubmissionBannerIsDisplayed(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391969
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        self.assertion.assertExists(self.requestQuote.getRFQSubmissionBanner(), 'Verify job submission banner is displayed')

    @pytest.mark.ac
    def testRequestQuoteButtonIsNotDisplayedForJobSubmittedForRFQ(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391971
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.assertion.assertNotExists(self.jobSummary.getRequestQuote().ui_object, 'Verify request quote button is not displayed')

    @pytest.mark.ac
    def testDeleteJobButtonIsNotDisplayedForJobSubmittedForRFQ(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1391975
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
        self.navigation.tapJobDetailBreadcrumb()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(3)
        self.navigation.tapJobBreadcrumb()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        try:
            deleteButton = self.jobList.getDeleteJobButton().ui_object
        except:
            deleteButton = None
        self.assertion.assertNotExists(deleteButton,'Verify delete job button is not displayed')

    @pytest.mark.ac
    def testJobSettingsCannotBeEditedAfterRFQSubmission(self):
        # Verify the job settings cannot be edited once an RFQ is submitted
        email = 'nick.moore+auto50@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1391972
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapOverflow()

        try:
            editSettings = self.jobList.getEditSettings().ui_object
        except:
            editSettings = None
        self.assertion.assertNotExists(editSettings, "Job settings button exists")

    @pytest.mark.ac
    def testJobReelsCannotBeEditedAfterRFQSubmission(self):
        # Verify the job reels cannot be edited once an RFQ is submitted
        email = 'nick.moore+auto50@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1391973
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()

        try:
            configureJob = self.jobSummary.getConfigureJob().ui_object
        except:
            configureJob = None

        self.assertion.assertNotExists(configureJob, "Configure job button exists")

    @pytest.mark.ac
    def testJobFeederScheduleCannotBeEditedAfterRFQSubmission(self):
        # Verify the job feeder schedule cannot be edited once an RFQ is submitted
        email = 'nick.moore+auto50@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1391974
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()

        try:
            configureJob = self.jobSummary.getConfigureJob().ui_object
        except:
            configureJob = None

        self.assertion.assertNotExists(configureJob, "Configure job button exists")



