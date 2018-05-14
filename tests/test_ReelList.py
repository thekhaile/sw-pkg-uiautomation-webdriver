from time import sleep
import pytest
import unidecode
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.reel import Reel


class TestReelList(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestReelList, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)

    @pytest.mark.ac
    # Verify that when no reels are created, the empty state screen for reel is displayed
    def testEmptyStateIsPresentedWhenNoReels(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381963
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        message = unidecode.unidecode(self.reelList.getEmptyState())

        self.assertion.assertEqual(message, "You haven't created any reels.")

    @pytest.mark.ac
    # Verify that when reels are freshly created, the smallest reel name "N7P" is displayed for Canadian users
    def testDefaultCAReelPackageIsN7P(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381965
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertEqual(self.reelList.getReelPackage(), "N7P")

    @pytest.mark.ac
    # Verify that when reels are freshly created with no circuit, the height/Width indicator is 0%
    def testNewReelVolumeDefaultToZeroPercent(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381967
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertEqual(self.reelList.getVolumePercentage(), "0%")

    @pytest.mark.ac
    # Verify that when reels are freshly created with no circuit, the weight indicator is 0%
    def testNewReelWeightDefaultToZeroPercent(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381968
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertEqual(self.reelList.getWeightPercentage(), "0%")

    @pytest.mark.ac
    # Verify that when Canadian reels are freshly created, the actual weight of the reel is displayed "30lbs"
    def testNewReelWeightDefaultTo30lbs(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381970
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertEqual(self.reelList.getWeightNumber(), "30LB.\n0%")

    @pytest.mark.ac
    # Verify that the first created reel is displayed at the top of the list of reel
    def testFirstCreatedReelIsOnTheTopOfReelList(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381976
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        oldValue = self.reelList.getReelName()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        newValue = self.reelList.getReelName()
        sleep(2)

        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    # Verify that the diameter (reel size) is displayed
    def testReelSizeIsDisplayed(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381980
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertExists(self.reelList.getReelSize())

    @pytest.mark.ac
    # Verify that the progress tracking for Volume is displayed
    def testVolumeBarIsDisplayed(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381985
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertExists(self.reelList.getVolumeBar())

    @pytest.mark.ac
    # Verify that the progress tracking for Weight is displayed
    def testWeightBarIsDisplayed(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1381983
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertExists(self.reelList.getWeightBar())

    @pytest.mark.ac
    # Verify that when reels are freshly created, the smallest reel name "N7" is displayed for US users
    def testDefaultUSReelPackageIsN7(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1381964
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertEqual(self.reelList.getReelPackage(), "N7")

    @pytest.mark.ac
    # Verify that when US reels are freshly created, the actual weight of the reel is displayed "50lbs"
    def testNewUSReelWeightDefaultTo50lbs(self):
        email = 'ningxin.liao+regression@mutualmobile.com'
        password = 'password'

        self.caseId = 1381969
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.reel.createReelWithNoRestriction()

        self.assertion.assertEqual(self.reelList.getWeightNumber(), "50LB.\n0%")