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
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
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
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)
        self.reels = Reels(self)
        self.circuit = Cricuit(self)

    def saveScreenshot(self, description):
        self.app.saveScreenshot(description + '_' + self.driver.desired_capabilities['browserName'] + '_' + self.driver.desired_capabilities['platform'], self.screenshotPath)

    @pytest.mark.ac1
    def testScreenshotFlow(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        '''Screenshot - Configurator - With circuit collapsed'''
        self.jobSummary.tapConfigureJob()
        self.saveScreenshot('flow_configurator_withCircuitCollapsed')
        '''Screenshot - Configurator - WIth circuit expanded'''
        self.feederSchedule.


