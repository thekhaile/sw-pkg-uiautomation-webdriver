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
import unidecode


class TestViewJobSummary(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestViewJobSummary, self).__init__(*args, **kwargs)
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

    @pytest.mark.ac
    def testJobTitleIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393651
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getJobNameOnViewJobSummary()
        self.assertion.assertEqual(el, '1')

    @pytest.mark.ac
    def testDateCreatedIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393652
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getDateCreated()
        self.assertion.assertEqual(el, '4/20/2018')

    @pytest.mark.ac
    def testDateModifiedIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393653
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getDateCreated()
        self.assertion.assertEqual(el, '4/20/2018')

    @pytest.mark.ac
    def testDateSentForRFQIsPresented(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393654
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.jobSummary.getQuoteSubmittedDate()
        self.assertion.assertEqual(el, '4/20/18')

    @pytest.mark.ac
    def testFromIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393655
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitFrom()
        self.assertion.assertEqual(el, 'a')

    @pytest.mark.ac
    def testToIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393656
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitTo()
        self.assertion.assertEqual(el, 'b')

    @pytest.mark.ac
    def testSizeIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393657
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitSize()
        self.assertion.assertEqual(el, '1')

    @pytest.mark.ac
    def testLengthIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393658
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitLength()
        self.assertion.assertEqual(el, "123'")

    @pytest.mark.ac
    def testReelIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393662
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        el = self.feederSchedule.getCircuitReelName()
        self.assertion.assertEqual(el, 'reel 1')

    @pytest.mark.ac
    def testConductorMetalIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393659
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.feederSchedule.tapExpandArrow()
        sleep(2)
        el = self.feederSchedule.getMetal()
        self.assertion.assertEqual(el, 'CU')

    @pytest.mark.ac
    def testConductorInsulationIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1396868
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.feederSchedule.tapExpandArrow()
        sleep(2)
        el = self.feederSchedule.getInsulation()
        self.assertion.assertEqual(el, 'THHN')

    @pytest.mark.ac
    def testConductorColorIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393660
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.feederSchedule.tapExpandArrow()
        sleep(2)
        el = self.feederSchedule.getColor()
        self.assertion.assertEqual(el, 'Green')

    @pytest.mark.ac1
    def testSIMpullHeadIsPresentedOnFeederSchedule(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393661
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.feederSchedule.tapExpandArrow()
        sleep(2)
        el = self.feederSchedule.getSIMpullHeadsText()

        self.assertion.assertExists(el)

    @pytest.mark.ac
    def testReelNameIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393663
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        el = self.reels.getReelName()
        self.assertion.assertEqual(el, 'reel 1')

    @pytest.mark.ac
    def testReelPackageIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393664
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        el = self.reels.getReelPackage()
        self.assertion.assertEqual(el, 'N7')

    @pytest.mark.ac
    def testReelSizeIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393665
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        el = unidecode.unidecode(self.reels.getReelSize())
        self.assertion.assertEqual(el, '30"')

    @pytest.mark.ac
    def testReelWeightIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393667
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        el = self.reels.getReelWeight()
        self.assertion.assertEqual(el, '87 lb')

    @pytest.mark.ac
    def testCircuitFromIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393669
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getCircuitFromOnReel()
        self.assertion.assertEqual(el, 'a')

    @pytest.mark.ac
    def testCircuitToIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393670
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getCircuitToOnReel()
        self.assertion.assertEqual(el, 'b')

    @pytest.mark.ac
    def testCircuitSizeIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393671
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getCircuitSizeOnReel()
        self.assertion.assertEqual(el, '1')

    @pytest.mark.ac
    def testCircuitLengthIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393672
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getCircuitLengthOnReel()
        self.assertion.assertEqual(el, "123'")

    @pytest.mark.ac
    def testCircuitMetalIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393674
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getCircuitMetal()
        self.assertion.assertEqual(el, 'CU')

    @pytest.mark.ac
    def testCircuitInsulationIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1396878
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getCircuitInsulation()
        self.assertion.assertEqual(el, 'THHN')

    @pytest.mark.ac
    def testCircuitColorIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393677
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getCircuitColor()
        self.assertion.assertEqual(el, 'Green')

    @pytest.mark.ac
    def testCorrectCircuitSIMpullHeadInfoIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393675
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getSIMpullHeadsText()

        self.assertion.assertExists(el)

    @pytest.mark.ac
    def testBullseyeVisualizationIsPresentedOnReelConfigurator(self):
        email = 'ningxin.liao+test4@mutualmobile.com'
        password = 'password'
        self.caseId = 1393678
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        self.reels.tapExpandArrow()
        sleep(2)
        el = self.reels.getBullseyeVisualization()
        self.assertion.assertExists(el)

    @pytest.mark.ac
    def testEmptyStateForFeederScheduleIsCorrect(self):
        email = 'ningxin.liao+testProjectList@mutualmobile.com'
        password = 'password'
        self.caseId = 1393683
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        el = unidecode.unidecode(self.feederSchedule.getFeederScheduleEmptyState())
        self.assertion.assertEqual(el, "You haven't configured a feeder schedule for this job yet.")

    @pytest.mark.ac
    def testEmptyStateForReelConfiguratorIsCorrect(self):
        email = 'ningxin.liao+testProjectList@mutualmobile.com'
        password = 'password'
        self.caseId = 1393684
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()
        sleep(2)
        self.reels.switchToReelsTab()
        sleep(2)
        el = unidecode.unidecode(self.reels.getReelsEmptyState())
        self.assertion.assertEqual(el, "You haven't configured reels for this job yet.")
