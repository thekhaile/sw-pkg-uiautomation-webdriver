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
from southwire_pkg_uiautomation_webdriver.components.jobSummary.feederSchedule import FeederSchedule as FeederScheduleOnJobSummary
from southwire_pkg_uiautomation_webdriver.components.jobSummary.reels import Reels
from southwire_pkg_uiautomation_webdriver.components.requestQuote import RequestQuote
from southwire_pkg_uiautomation_webdriver.components.registration import Registration
from southwire_pkg_uiautomation_webdriver.components.passwordReset import PasswordReset
import unidecode


class TestScreenshotFlow2(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestScreenshotFlow2, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        self.feederScheduleOnJobSummary = FeederScheduleOnJobSummary(self)
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)
        self.reels = Reels(self)
        self.requestQuote = RequestQuote(self)
        self.registration = Registration(self)
        self.passwordReset = PasswordReset(self)


    def saveScreenshot(self, description):
        self.app.saveScreenshot(description + '_' + self.driver.desired_capabilities['browserName'] + '_' + self.driver.desired_capabilities['platform'], self.screenshotPath)

    @pytest.mark.ac
    def testScreenshotFlow(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        """Screenshot - Configurator - With circuit collapsed"""
        self.jobSummary.tapConfigureJob()
        self.saveScreenshot('flow_configurator_WithCircuitCollapsed')
        sleep(2)
        """Screenshot - Configurator - WIth circuit expanded"""
        self.feederSchedule.tapExpandArrow()
        self.saveScreenshot('flow_configurator_WithCircuitExpanded')
        sleep(2)
        """Screenshot - Create Reel - Empty"""
        self.reelList.tapCreateReel()
        self.saveScreenshot('flow_createReel_Empty')
        sleep(2)
        """Screenshot - Configurator - with reel list and circuit"""
        self.reel.enterRandomReelName()
        sleep(2)
        self.reel.tapSubmit()
        sleep(2)
        self.saveScreenshot('flow_configurator_WithReelListAndCircuit')
        sleep(2)
        """Screenshot - Configurator - Circuits on Reel Empty"""
        self.feederSchedule.switchToCircuitsOnReelTab()
        self.saveScreenshot('flow_configurator_CircuitsOnReelEmpty')
        sleep(2)
        """Screenshot - Configurator - Circuits on Reel with circuits"""
        self.feederSchedule.switchToAvailableCircuitTab()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.switchToCircuitsOnReelTab()
        self.saveScreenshot('flow_configurator_CircuitsOnReelWithCircuits')
        sleep(2)
        """Screenshot - Job Summary - Feeder Schedule collapsed"""
        self.navigation.tapJobBreadcrumb()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_FeederScheduleCollapsed')
        sleep(2)
        """Screenshot - Job Summary - Feeder Schedule expanded"""
        self.feederScheduleOnJobSummary.tapExpandArrow()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_FeederScheduleExpanded')
        sleep(2)
        """Job Summary - Reel collapsed"""
        self.reels.switchToReelsTab()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_ReelCollapsed')
        sleep(2)
        """Job Summary - Reel expanded"""
        self.reels.tapExpandArrow()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_ReelExpanded')
        sleep(2)
        """Job summary - Circuits on reel expanded"""
        self.reels.tapExpandArrow()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_CircuitOnReelExpanded')
        sleep(2)
        """Request for Quote - Empty"""
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.saveScreenshot('flow_requestForQuote_Empty')
        sleep(2)
        """Job Summary - RFQ Submited"""
        self.requestQuote.tapSubmit()
        sleep(2)
        self.saveScreenshot('flow_jobSummary_RFQSubmited')
        sleep(2)
        self.navigation.navigateToProjectsPage()
        sleep(2)
        """Job list - Quote sent"""
        self.projectList.selectAProject()
        sleep(2)
        self.saveScreenshot('flow_jobList_quoteSent')
        sleep(2)
        """Account page"""
        self.registration.tapAccount()
        sleep(2)
        self.saveScreenshot('flow_accountPage')

    @pytest.mark.ac
    def testScreenshotFlowForgotPassword(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'

        self.navigation.navigateToLoginPage()
        sleep(2)
        self.authentication.tapForgotPassword()
        sleep(2)
        """Forgot Password - Empty"""
        self.saveScreenshot('flow_forgotPassword_Empty')
        sleep(2)
        """Forgot Password - Error"""
        self.passwordReset.enterEmail('ningxin.com')
        self.passwordReset.tapReset()
        sleep(2)
        self.saveScreenshot('flow_forgotPassword_Error')
        sleep(2)
        """Log in - Password reset email sent"""
        self.passwordReset.enterEmail(email)
        self.passwordReset.tapReset()
        sleep(2)
        self.saveScreenshot('flow_logIn_PasswordResetEmailSent')