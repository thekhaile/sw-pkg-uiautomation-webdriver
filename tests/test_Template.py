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
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit

class TestTemplate(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestTemplate, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)
        self.circuit = Circuit(self)

    @pytest.mark.ac
    def testUploadTemplateOptionAvailableFreshJob(self):
        # Verify the upload template option is available for freshly created job
        email = 'nick.moore+auto29@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381715
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()

        self.assertion.assertExists(self.jobSummary.getUploadTemplateOption(), "Upload template option not available")

    @pytest.mark.ac
    def testUploadTemplateOptionAvailableInProgressJob(self):
        # Verify the upload template option is available for an in progress job
        email = 'nick.moore+auto30@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381716
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.reel.createReelWithNoRestriction()
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        self.jobList.selectAJob()

        self.assertion.assertExists(self.jobSummary.getUploadTemplateOption(), "Upload template option not available")

    @pytest.mark.ac
    def testUploadTemplateOptionAfterCircuitsRemoved(self):
        # Verify the upload template option is available when all circuits have been removed from feeder schedule
        email = 'nick.moore+auto31@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381717
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createLargeUSCircuit()
        sleep(1)
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapDeleteCircuit()
        self.feederSchedule.tapConfirmDelete()
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(1)

        self.assertion.assertExists(self.jobSummary.getUploadTemplateOption(), "Upload template option not available")

    @pytest.mark.ac
    def testUploadTemplateOptionNotAvailableAfterRFQ(self):
        # Verify the upload template option isn't available after submitting for RFQ
        email = 'nick.moore+auto32@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381718
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()

        self.assertion.assertNotExists(self.jobSummary.getUploadTemplateOption(), "Upload template option is available")

    @pytest.mark.ac
    def testUploadTemplateOptionNotAvailableIfCircuitsInJob(self):
        # Verify the upload template option is not available for jobs that have existing circuits
        email = 'nick.moore+auto33@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381719
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        self.circuit.createCircuitWithSIMpullHead()
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        self.jobList.selectAJob()

        self.assertion.assertNotExists(self.jobSummary.getUploadTemplateOption(), "Upload template option is available")

    @pytest.mark.ac
    def testUploadOptionHiddenAfterSuccessfulUpload(self):
        # Verify the upload option is hidden and not able to re-upload the template again after a successful upload
        email = 'nick.moore+auto34@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381720
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')

        self.assertion.assertNotExists(self.jobSummary.getUploadTemplateOption(), "Upload template option is available")



