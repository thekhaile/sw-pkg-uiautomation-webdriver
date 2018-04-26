from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.project import Project
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule


class TestTrackReelProgress(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestTrackReelProgress, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.project = Project(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.jobSummary = JobSummary(self)
        self.circuit = Circuit(self)
        self.reel = Reel(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        
    @pytest.mark.ac
    def testReelWithNoCircuitCanBeDeleted(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1388821
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reelList.getReelName()
        self.reel.createReelWithNoRestriction()
        sleep(3)
        # end of precondition
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapDeleteReel()
        sleep(2)
        self.reelList.tapConfirmDelete()
        newValue = self.reelList.getReelName()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testReelWithOneCircuitCanBeDeleted(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1388822
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reelList.getReelName()
        self.circuit.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        # end of precondition
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapDeleteReel()
        sleep(2)
        self.reelList.tapConfirmDelete()
        newValue = self.reelList.getReelName()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testReelWithMoreThanOneCircuitCanBeDeleted(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1388823
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.project.createAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reelList.getReelName()
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        # end of precondition
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapDeleteReel()
        sleep(2)
        self.reelList.tapConfirmDelete()
        newValue = self.reelList.getReelName()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testVolumeIsTrackForCurrentLoad(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381492
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reelList.getVolumePercentage()
        # end of precondition
        self.circuit.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testWeightIsTrackForCurrentLoad(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381493
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reelList.getWeightPercentage()
        # end of precondition
        self.circuit.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reelList.getWeightPercentage()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasNoRestrictionOnUSNonSIMpullReel(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381494
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeUSCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reelList.getReelPackage()

        self.assertion.assertEqual(package, 'A62R')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasNoRestrictionOnCANonSIMpullReel(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381495
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeCACircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reelList.getReelPackage()

        self.assertion.assertEqual(package, 'A62R')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasNoRestrictionOnSIMpullReel(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1381496
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createSIMpullReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeCASIMpullCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reelList.getReelPackage()

        self.assertion.assertEqual(package, 'SIM61')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasOverLimitRestrictionsOnUSNonSIMpullReel(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381497
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelOverRestrictions()
        sleep(3)
        self.circuit.createLargeUSCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reelList.getReelPackage()

        self.assertion.assertEqual(package, 'A62R')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenHeightIsTheLimitingFactor(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381502
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithHeightRestrictionOf31()
        sleep(3)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getExceedsAlert()
        package = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertEqual(package, 'N7')
        self.assertion.assertEqual(weight, '77%')
        self.assertion.assertEqual(volume, '94%')
        self.assertion.assertExists(alert.ui_object)

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenWidthIsTheLimitingFactor(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381505
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithWidthRestrictionOf21()
        sleep(3)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getExceedsAlert()
        package = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertEqual(package, 'N7')
        self.assertion.assertEqual(weight, '77%')
        self.assertion.assertEqual(volume, '94%')
        self.assertion.assertExists(alert.ui_object)

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenWeightIsTheLimitingFactor(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381508
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithWeightRestrictionOf1000()
        sleep(3)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getExceedsAlert()
        package = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertEqual(package, 'N7')
        self.assertion.assertEqual(weight, '77%')
        self.assertion.assertEqual(volume, '94%')
        self.assertion.assertExists(alert.ui_object)

    @pytest.mark.ac
    def testReelSizeIncreaseWhenExceedCurrentVolumeCapacity(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381511
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'N25F')
        self.assertion.assertEqual(weight, '58%')
        self.assertion.assertEqual(volume, '52%')

    @pytest.mark.ac
    def testReelSizeIncreaseBy2WhenExceedCurrentVolumeCapacityUS(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381513
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createMediumUSCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'R16')
        self.assertion.assertEqual(weight, '70%')
        self.assertion.assertEqual(volume, '44%')

    @pytest.mark.ac
    def testReelSizeIncreaseWhenExceedCurrentWeightCapacity(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381516
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'N25F')
        self.assertion.assertEqual(weight, '58%')
        self.assertion.assertEqual(volume, '52%')

    @pytest.mark.ac
    def testReelSizeIncreaseBy2WhenExceedCurrentVolumeCapacityCA(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381518
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeCACircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'A62R')
        self.assertion.assertEqual(weight, '94%')
        self.assertion.assertEqual(volume, '96%')

    @pytest.mark.ac
    def testSIMpullReelSizeIncreaseWhenExceedCurrentWeightCapacity(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1381520
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createSIMpullReelWithNoRestriction()
        sleep(3)
        oldValue = self.reelList.getReelPackage()
        self.circuit.createLargeCASIMpullCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'SIM61')
        self.assertion.assertEqual(weight, '93%')
        self.assertion.assertEqual(volume, '68%')

    @pytest.mark.ac
    def testReelSizeDecreaseWhenBelowCurrentVolumeCapacity(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381522
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createMiniUSCircuit()
        sleep(2)
        self.circuit.createMiniUSCircuit()
        sleep(2)
        self.circuit.createMiniUSCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        # end of precondition
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        self.feederSchedule.confirmRemoval()
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'N7')
        self.assertion.assertEqual(weight, '79%')
        self.assertion.assertEqual(volume, '99%')

    @pytest.mark.ac
    def testReelSizeDecreaseBy2WhenBelowCurrentVolumeCapacity(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381524
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeUSCircuit()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        # end of precondition
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        self.feederSchedule.confirmRemoval()
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'N7')
        self.assertion.assertEqual(weight, '0%')
        self.assertion.assertEqual(volume, '0%')

    @pytest.mark.ac
    def testReelSizeDecreaseBy2WhenBelowCurrentVolumeCapacity(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381529
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeCACircuit()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        # end of precondition
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        self.feederSchedule.confirmRemoval()
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'N7P')
        self.assertion.assertEqual(weight, '0%')
        self.assertion.assertEqual(volume, '0%')

    @pytest.mark.ac
    def testSIMpullReelSizeDecreaseWhenExceedCurrentWeightCapacity(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1381530
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createSIMpullReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeCASIMpullCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        sleep(2)
        self.feederSchedule.confirmRemoval()
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'SIM51')
        self.assertion.assertEqual(weight, '0%')
        self.assertion.assertEqual(volume, '0%')

    @pytest.mark.ac
    def testCircuitsCanBeAddToReelUntilExceedVolumeCapacity(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381534
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(3)
        self.circuit.createLargeCACircuit()
        sleep(2)
        self.circuit.createLargeCACircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reelList.getReelPackage()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.getExceedsAlert()
        newValue = self.reelList.getReelPackage()
        weight = self.reelList.getWeightPercentage()
        volume = self.reelList.getVolumePercentage()

        self.assertion.assertEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'A62R')
        self.assertion.assertEqual(weight, '94%')
        self.assertion.assertEqual(volume, '96%')