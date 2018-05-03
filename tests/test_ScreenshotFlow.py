from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.passwordReset import PasswordReset
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.project import Project
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components import Registration
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components import Reels
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.feederSchedule import FeederSchedule as FeederScheduleOnJobSummary
from southwire_pkg_uiautomation_webdriver.components.requestQuote import RequestQuote

class TestScreenshotFlow(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestScreenshotFlow, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.passwordReset = PasswordReset(self)
        self.projectList = ProjectList(self)
        self.project = Project(self)
        self.jobList = JobList(self)
        self.job = Job(self)
        self.jobSummary = JobSummary(self)
        self.feederSchedule = FeederSchedule(self)
        self.circuit = Circuit(self)
        self.registration = Registration(self)
        self.reel = Reel(self)
        self.reels = Reels(self)
        self.reelList = ReelList(self)
        self.feederScheduleOnJobSummary = FeederScheduleOnJobSummary(self)
        self.requestQuote = RequestQuote(self)

    def saveScreenshot(self, description):
        if self.app.isFirefox:
            platform = ''
        else:
            platform = self.driver.desired_capabilities['platform']

        self.app.saveScreenshot(description + '_' + self.driver.desired_capabilities['browserName'] + '_' + platform,
                                self.screenshotPath)

    @pytest.mark.ac
    def testScreenShotFlow(self):
        # Screenshot - Login page empty state
        self.navigation.navigateToLoginPage()
        sleep(1)
        self.saveScreenshot('flow_login_Empty')

        # Screenshot - Login page error
        email = 'nick.moore+testflowmutualmobile.com'
        password = 'newpassword'
        self.authentication.login(email, password)
        self.saveScreenshot('flow_login_Error')

        # Log in successfully
        email = 'nick.moore+testflow@mutualmobile.com'
        password = 'newpassword'
        self.authentication.login(email, password)

        # Screenshot - Project List
        self.saveScreenshot('flow_projectList')

        # Screenshot - Create project empty state
        self.projectList.tapCreateProject()
        self.saveScreenshot('flow_createProject_Empty')

        # Screenshot - Create project error
        self.project.enterProjectName('Project1')
        self.project.tapSubmit()
        sleep(1)
        self.saveScreenshot('flow_createProject_Error')

        # Create a project
        self.project.enterRandomProjectName()
        self.project.tapSubmit()

        # Screenshot - Job list empty state
        self.projectList.selectAProject()
        sleep(1)
        self.saveScreenshot('flow_jobList_Empty')

        # Screenshot - Create job empty state
        self.jobList.tapCreateJob()
        sleep(1)
        self.saveScreenshot('flow_createJob_Empty')

        # Create a job
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        self.job.tapSubmit()
        sleep(1)

        # Screenshot - Job list
        self.saveScreenshot('flow_jobList')

        # Screenshot - Create job error
        self.jobList.tapCreateJob()
        self.job.enterJobName(jobName)
        self.job.tapSubmit()
        self.saveScreenshot('flow_createJob_Error')
        sleep(1)

        # Screenshot - Job Summary Feeder schedule empty
        self.job.tapCancel()
        self.jobList.selectAJob()
        self.saveScreenshot('flow_jobSummaryFeederSchedule_Empty')

        # Screenshot - Job Summary reels empty
        self.reels.switchToReelsTab()
        self.saveScreenshot('flow_jobSummaryReels_Empty')

        # Screenshot - RFQ error
        self.jobSummary.tapRequestQuote()
        sleep(1)
        self.saveScreenshot('flow_jobSummary_RFQError')

        # Screenshot - Configurator empty
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.saveScreenshot('flow_configurator_Empty')

        # Screenshot - Create circuit empty
        self.feederSchedule.tapCreateCircuit()
        sleep(1)
        self.saveScreenshot('flow_createCircuit_Empty')

        # Screenshot - Create circuit filled out
        self.circuit.enterRandomFrom()
        self.circuit.enterRandomTo()
        self.circuit.selectConductorType(type='CU / THHN')
        self.circuit.selectConductorSize(size='1')
        self.circuit.enterCircuitLength('100')
        self.circuit.toggleSIMpullHead()
        self.circuit.selectNumOfConductor(NOC='4')
        self.circuit.selectCommonPreset(preset='Pink-Purple-Tan-Gray')
        sleep(1)
        self.saveScreenshot('flow_createCircuit_Filled')
        sleep(2)
        self.circuit.tapSubmit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)

        # Screenshot - Configurator - With circuit collapsed
        self.saveScreenshot('flow_configurator_WithCircuitCollapsed')
        sleep(2)

        # Screenshot - Configurator - WIth circuit expanded
        self.feederSchedule.tapExpandArrow()
        self.saveScreenshot('flow_configurator_WithCircuitExpanded')
        sleep(2)

        # Screenshot - Create Reel - Empty
        self.reelList.tapCreateReel()
        self.saveScreenshot('flow_createReel_Empty')
        sleep(2)

        # Screenshot - Configurator - with reel list and circuit
        self.reel.enterRandomReelName()
        sleep(2)
        self.reel.tapSubmit()
        sleep(2)
        self.saveScreenshot('flow_configurator_WithReelListAndCircuit')
        sleep(2)

        # Screenshot - Configurator - Circuits on Reel Empty
        self.feederSchedule.switchToCircuitsOnReelTab()
        self.saveScreenshot('flow_configurator_CircuitsOnReelEmpty')
        sleep(2)

        # Screenshot - Configurator - Circuits on Reel with circuits
        self.feederSchedule.switchToAvailableCircuitTab()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.switchToCircuitsOnReelTab()
        self.saveScreenshot('flow_configurator_CircuitsOnReelWithCircuits')
        sleep(2)

        # Screenshot - Job Summary - Feeder Schedule collapsed
        self.navigation.tapJobBreadcrumb()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_FeederScheduleCollapsed')
        sleep(2)

        # Screenshot - Job Summary - Feeder Schedule expanded
        self.feederScheduleOnJobSummary.tapExpandArrow()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_FeederScheduleExpanded')
        sleep(2)

        # Job Summary - Reel collapsed
        self.reels.switchToReelsTab()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_ReelCollapsed')
        sleep(2)

        # Job Summary - Reel expanded
        self.reels.tapExpandArrow()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_ReelExpanded')
        sleep(2)

        # Job summary - Circuits on reel expanded
        self.reels.tapExpandArrow()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_CircuitOnReelExpanded')
        sleep(2)

        # Request for Quote - Empty
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.saveScreenshot('flow_requestForQuote_Empty')
        sleep(2)

        # Job Summary - RFQ Submited
        self.requestQuote.tapSubmit()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_RFQSubmited')
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)

        # Job list - Quote sent
        self.projectList.selectAProject()
        sleep(2)
        self.saveScreenshot('flow_jobList_quoteSent')
        sleep(2)

        # Account page
        self.registration.tapAccount()
        sleep(2)
        self.saveScreenshot('flow_accountPage')

    @pytest.mark.ac
    def testScreenshotFlowAccountCreation(self):
        self.navigation.navigateToLoginPage()
        self.authentication.tapCreateAccount()

        # Screenshot - Create account empty
        self.saveScreenshot('flow_createAccount_Empty')

        # Create account with error
        self.registration.enterEmail('nick.moore+auto1@mutualmobile.com')
        self.registration.enterPassword('newpassword')
        self.registration.enterConfirmPassword('mismatch')
        self.registration.enterRandomName()
        self.registration.enterCompanyName('MM')
        self.registration.selectRandomRole()
        self.registration.enterCity('Austin')
        self.registration.selectStateOrProvince('Texas')
        self.registration.tapSubmit()

        # Screenshot - Create account error
        self.driver.execute_script("window.scrollTo(0, 0);")
        sleep(1)
        self.saveScreenshot('flow_createAccount_Error')

        # Create account
        self.navigation.navigateToRegistrationPage()
        self.registration.enterEmail(self.registration.generateRandomEmail())
        self.registration.enterPassword('newpassword')
        self.registration.enterConfirmPassword('newpassword')
        self.registration.enterRandomName()
        self.registration.enterCompanyName('MM')
        self.registration.selectRandomRole()
        self.registration.enterCity('Austin')
        self.registration.selectStateOrProvince('Texas')
        self.registration.tapSubmit()
        if self.app.isFirefox():
            sleep(2)
            self.app.driver.switch_to_alert().accept()
        sleep(2)

        # Screenshot - Login account created
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.saveScreenshot('flow_login_accountCreated')

    @pytest.mark.ac
    def testScreenshotFlowForgotPassword(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'

        self.navigation.navigateToLoginPage()
        sleep(2)
        self.authentication.tapForgotPassword()
        sleep(2)
        # Forgot Password - Empty
        self.saveScreenshot('flow_forgotPassword_Empty')
        sleep(2)

        # Forgot Password - Error
        self.passwordReset.enterEmail('ningxin@com')
        self.passwordReset.tapReset()
        sleep(2)
        self.saveScreenshot('flow_forgotPassword_Error')
        sleep(2)

        # Log in - Password reset email sent
        self.passwordReset.enterEmail(email)
        self.passwordReset.tapReset()
        sleep(2)
        self.saveScreenshot('flow_logIn_PasswordResetEmailSent')

    @pytest.mark.ac
    def testScreenshotFlowDeleteJob(self):
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail('nick.moore+testflow@mutualmobile.com')
        self.authentication.enterPassword('newpassword')
        self.authentication.tapSubmit()
        self.projectList.selectAProject()
        self.job.createAJob()

        # Screenshot - overflow menu on job summary
        self.jobList.tapOverflow()
        sleep(1)
        self.saveScreenshot('flow_deleteJob_Overflow')

        # Screenshot - delete confirmation modal
        self.jobList.tapDeleteJob()
        sleep(1)
        self.saveScreenshot('flow_deleteJob_Confirmation')

        self.jobList.tapConfirmDelete()

        # Screenshot - Post job deletion
        sleep(1)
        self.saveScreenshot('flow_deleteJob_After')

    @pytest.mark.ac
    def testScreenshotFlowCircuitDeletion(self):
        email = 'nick.moore+testflow@mutualmobile.com'
        password = 'newpassword'

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

        # Circuit deletion - selecte a circuit
        self.saveScreenshot('flow_circuitDeletion_SelecteACircuit')
        sleep(2)

        # Circuit deletion - deletion confirmation
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapDeleteCircuit()
        sleep(2)
        self.saveScreenshot('flow_circuitDeletion_DeletionConfirmation')
        sleep(2)

        # Circuit deletion - after deletion
        self.feederSchedule.tapConfirmDelete()
        sleep(2)
        self.saveScreenshot('flow_circuitDeletion_AfterDeletion')

    @pytest.mark.ac
    def testScreenshotFlowReelDeletion(self):
        email = 'nick.moore+testflow@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(2)

        # Reel deletion - selecte a reel
        self.saveScreenshot('flow_reelDeletion_SelecteAReel')
        sleep(2)

        # Reel deletion - deletion confirmation
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapDeleteReel()
        sleep(2)
        self.saveScreenshot('flow_reelDeletion_DeletionConfirmation')
        sleep(2)

        # Reel deletion - after deletion
        self.reelList.tapConfirmDelete()
        sleep(2)
        self.saveScreenshot('flow_reelDeletion_AfterDeletion')

    @pytest.mark.ac
    def testScreenshotFlowRemoveCircuit(self):
        self.navigation.navigateToLoginPage()
        self.authentication.enterEmail('nick.moore+testflow@mutualmobile.com')
        self.authentication.enterPassword('newpassword')
        self.authentication.tapSubmit()
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()

        # Create a reel with one circuit
        self.reel.createReelWithNoRestriction()
        sleep(1)
        self.circuit.createLargeUSCircuit()
        self.feederSchedule.tapAddCircuit()
        sleep(1)

        # Screenshot - Remove circuit from reel confirmation
        self.feederSchedule.switchToCircuitsOnReelTab()
        self.feederSchedule.tapRemoveCircuit()
        sleep(1)
        self.saveScreenshot('flow_removeCircuit_Confirmation')

        # Screenshot - After circuit removed
        self.feederSchedule.tapConfirmDelete()
        sleep(1)
        self.saveScreenshot('flow_removeCircuit_After')
