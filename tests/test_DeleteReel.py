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


class TestDeleteReel(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestDeleteReel, self).__init__(*args, **kwargs)
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
    def testDeleteButtonIsEnabledForInProgressJob(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388819
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
        button = self.reelList.getDeleteButton()

        self.assertion.assertExists(button.ui_object)

    @pytest.mark.ac
    def testDeleteReelIsDisabledForJobSubmittedForRFQ(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388820
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
    def testConfirmationModalIsDisplayedUponDeleteButton(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388824
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
        self.reelList.tapDeleteReel()
        sleep(2)
        modal = self.reelList.getConfirmationModal()
        text = self.reelList.getConfirmationModal().getLabel()
        self.assertion.assertExists(modal.ui_object)
        self.assertion.assertEqual(text, 'Are you sure you want to delete this reel?')

    @pytest.mark.ac
    def testReelIsDeletedFromReelListAfterConfirmDeletion(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388825
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
        self.reel.createReelWithNoRestriction()
        sleep(2)
        oldValue = self.reelList.getReelName()
        oldLen = len(self.reelList.getReels())
        """end of preconditions"""
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapDeleteReel()
        sleep(2)
        self.reelList.tapConfirmDelete()
        sleep(2)
        newValue = self.reelList.getReelName()
        newLen = len(self.reelList.getReels())
        sleep(2)
        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(oldLen, newLen + 1)

    @pytest.mark.ac
    def testCircuitBeenPlacedOnAReelBecomeAvailableAfterReelIsDeleted(self):
        email = 'ningxin.liao+regression3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388826
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
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        oldValue = self.feederSchedule.getCircuitFrom()
        """end of preconditions"""
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapDeleteReel()
        sleep(2)
        self.reelList.tapConfirmDelete()
        sleep(2)
        self.feederSchedule.switchToAvailableCircuitTab()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom()
        self.assertEqual(oldValue, newValue)
