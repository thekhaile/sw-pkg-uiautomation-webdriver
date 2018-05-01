from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components.requestQuote import RequestQuote


class TestEditReelSettings(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestEditReelSettings, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.reel = Reel(self)
        self.jobSummary = JobSummary(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.circuit = Circuit(self)
        self.feederSchedule = FeederSchedule(self)
        self.requestQuote = RequestQuote(self)

    @pytest.mark.ac
    def testEditButtonIsEnabledForInProgressJob(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1381674
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        """end of preconditions"""
        self.reelList.tapOverflow()
        sleep(2)
        button = self.reelList.getEditButton()

        self.assertion.assertExists(button.ui_object)

    @pytest.mark.ac
    def testEditReelIsDisabledForJobSubmittedForRFQ(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1381675
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        """end of preconditions"""
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(2)
        button = self.jobSummary.getConfigureJob()

        self.assertion.assertNotExists(button.ui_object)

    @pytest.mark.ac
    def testHeightIsDisplayedOnEditReelSettingsPage(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1381677
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelOverRestrictions()
        sleep(2)
        """end of precondition"""
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapEditReel()
        sleep(2)
        el = self.reel.getHeightInput()

        self.assertion.assertEqual(el, '999999"')

    @pytest.mark.ac
    def testWidthIsDisplayedOnEditReelSettingsPage(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1381679
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelOverRestrictions()
        sleep(2)
        """end of precondition"""
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapEditReel()
        sleep(2)
        el = self.reel.getWidthInput()

        self.assertion.assertEqual(el, '999999"')

    @pytest.mark.ac
    def testWeightIsDisplayedOnEditReelSettingsPage(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1381681
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelOverRestrictions()
        sleep(2)
        """end of precondition"""
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapEditReel()
        sleep(2)
        el = self.reel.getWeightInput()

        self.assertion.assertEqual(el, '999999lb')

    @pytest.mark.ac
    def testSaveButtonIsEnabledWhenConditionsMet(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1381691
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelOverRestrictions()
        sleep(2)
        """end of precondition"""
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapEditReel()
        sleep(2)
        self.reel.enterRandomReelName()
        el = self.reel.getSubmitButton()

        self.assertion.assertTrue(el.isEnabled())