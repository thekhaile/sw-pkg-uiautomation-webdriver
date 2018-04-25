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
import unidecode

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

    @pytest.mark.ac
    def testVerifyUploadedCircuitsDisplayedInOrder(self):
        # Verify that uploaded circuits are displayed in order
        email = 'nick.moore+auto35@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381722
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        fromList = ['PANEL', 'PANEL', 'MCC-1', 'MCC-1']
        toList = ['GEN-ATS-U', 'GEN-ATS-I #1', 'XFRMT T1', 'XFRMT T1']
        sizeList = ['400', '350', '6', '8']
        lengthList = ["359'", "379'", "180'", "180'"]

        rowCount = self.feederSchedule.getNumberOfRows()
        for i in range(rowCount):
            self.assertion.assertEqual(self.feederSchedule.getCircuitFrom(i), fromList[i], "Circuit FROM does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitTo(i), toList[i], "Circuit TO does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitSize(i), sizeList[i], "Circuit SIZE does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitLength(i), lengthList[i], "Circuit LENGTH does not match")

    @pytest.mark.ac
    def testVerifyUploadedCircuitsCanBeEdited(self):
        # Verify that uploaded circuits can be edited
        email = 'nick.moore+auto36@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381738
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapEditCircuit()
        self.circuit.enterCircuitLength('1000')
        self.circuit.tapSubmit()

        self.assertion.assertEqual(self.feederSchedule.getCircuitLength(0), "1000'", "Circuit LENGTH does not match")

    @pytest.mark.ac
    def testVerifyUploadedCircuitsCanBeDuplicated(self):
        # Verify uploaded circuits can be duplicated
        email = 'nick.moore+auto37@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381739
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        beforeRowCount = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapDuplicateCircuit()
        afterRowCount = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(beforeRowCount + 1, afterRowCount, "Row count after duplication is wrong")

    @pytest.mark.ac
    def testVerifyUploadedCircuitsCanBeDeleted(self):
        # Verify uploaded circuits can be Deleted
        email = 'nick.moore+auto38@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381740
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        beforeRowCount = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapDeleteCircuit()
        self.feederSchedule.tapConfirmDelete()
        afterRowCount = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(beforeRowCount - 1, afterRowCount, "Row count after deletion is wrong")

    @pytest.mark.ac
    def testUploadedCircuitsSIMpullHeadDefaultOff(self):
        # Verify that SIMpull head is set to Off by default for uploaded circuits
        email = 'nick.moore+auto39@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381737
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        self.feederSchedule.tapOverflow()
        sleep(1)
        self.feederSchedule.tapEditCircuit()
        sleep(1)

        self.assertion.assertFalse(self.circuit.getSIMpullHeadToggle().isOn(), "SIMpull head is not set to off")

    @pytest.mark.ac
    def testUploadedCircuitsHaveCorrectGroundMetal(self):
        # Verify that uploaded circuits have the correct ground metal selected
        email = 'nick.moore+auto40@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381735
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        # 4th circuit position is the ground
        self.feederSchedule.tapOverflow(3)
        sleep(1)
        self.feederSchedule.tapEditCircuit(3)

        self.assertion.assertEqual(self.circuit.getConductorTypePicker().getValue(), 'CU|THHN', "Circuit conductor type doesn't match")

    @pytest.mark.ac
    def testCircuitsCanBeAddedAfterTemplateUpload(self):
        # Verify that circuits can be added to feeder schedule after template upload
        email = 'nick.moore+auto41@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381741
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        beforeCount = self.feederSchedule.getNumberOfRows()
        self.circuit.createLargeUSCircuit()
        afterCount = self.feederSchedule.getNumberOfRows()

        self.assertion.assertEqual(beforeCount + 1, afterCount, 'Number of rows mismatch')

    @pytest.mark.ac
    def testVerifyGroundSizeAfterTemplateUpload(self):
        # Verify that the correct ground size is displayed on feeder schedule according to the template
        email = 'nick.moore+auto42@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381736
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()

        self.assertion.assertEqual(self.feederSchedule.getCircuitSize(3), '8', 'Ground size is not 8')

    @pytest.mark.ac
    def testVerifyGroundWireSharesSameFromAsCircuit(self):
        # Verify that ground wire is a separate circuit that shares the same From of the main circuit in the same row
        email = 'nick.moore+auto44@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381727
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        fromValue = self.feederSchedule.getCircuitFrom(3)

        self.assertEqual(fromValue, 'MCC-1', 'FROM value for ground wire does not match paired circuit')

    @pytest.mark.ac
    def testVerifyGroundWireSharesSameToAsCircuit(self):
        # Verify that ground wire is a separate circuit that shares the same To of the main circuit in the same row
        email = 'nick.moore+auto45@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381728
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        toValue = self.feederSchedule.getCircuitTo(3)

        self.assertEqual(toValue, 'XFRMT T1', 'TO value for ground wire does not match paired circuit')

    @pytest.mark.ac
    def testVerifyGroundWireSharesSameLengthAsCircuit(self):
        # Verify that ground wire is a separate circuit that shares the same Length of the main circuit in the same row
        email = 'nick.moore+auto46@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381729
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        self.jobSummary.uploadTemplate('/../../test_data/Example_upload.xlsm')
        sleep(2)
        self.jobSummary.tapConfigureJob()
        length = self.feederSchedule.getCircuitLength(3)

        self.assertEqual(length, "180'", 'LENGTH value for ground wire does not match paired circuit')
