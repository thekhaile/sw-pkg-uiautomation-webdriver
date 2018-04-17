__author__ = 'ningxinliao'
import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects
from southwire_pkg_uiautomation_webdriver.components.jobs import Jobs
from southwire_pkg_uiautomation_webdriver.components.circuits import Circuits
from southwire_pkg_uiautomation_webdriver.components.reels import Reels
from southwire_pkg_uiautomation_webdriver.components.feederSchedule import FeederSchedule
import unidecode

class TestTrackReelProgress(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestTrackReelProgress, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)
        self.jobs = Jobs(self)
        self.circuits = Circuits(self)
        self.reels = Reels(self)
        self.feederSchedule = FeederSchedule(self)
        
    @pytest.mark.ac
    def testReelWithNoCircuitCanBeDeleted(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1388821
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reels.getReelName()
        self.reels.createReelWithNoRestriction()
        sleep(3)
        # end of precondition
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapDeleteReel()
        sleep(2)
        self.reels.tapConfirmDelete()
        newValue = self.reels.getReelName()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testReelWithOneCircuitCanBeDeleted(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1388822
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reels.getReelName()
        self.circuits.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        # end of precondition
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapDeleteReel()
        sleep(2)
        self.reels.tapConfirmDelete()
        newValue = self.reels.getReelName()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testReelWithMoreThanOneCircuitCanBeDeleted(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1388823
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.createAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reels.getReelName()
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        # end of precondition
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapDeleteReel()
        sleep(2)
        self.reels.tapConfirmDelete()
        newValue = self.reels.getReelName()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testVolumeIsTrackForCurrentLoad(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381492
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reels.getVolumePercentage()
        # end of precondition
        self.circuits.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reels.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testWeightIsTrackForCurrentLoad(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381493
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        oldValue = self.reels.getWeightPercentage()
        # end of precondition
        self.circuits.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reels.getWeightPercentage()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasNoRestrictionOnUSNonSIMpullReel(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381494
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeUSCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reels.getReelPackage()

        self.assertion.assertEqual(package, 'A62R')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasNoRestrictionOnCANonSIMpullReel(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381495
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeCACircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reels.getReelPackage()

        self.assertion.assertEqual(package, 'A62R')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasNoRestrictionOnSIMpullReel(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1381496
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createSIMpullReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeCASIMpullCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reels.getReelPackage()

        self.assertion.assertEqual(package, '61"')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenReelHasOverLimitRestrictionsOnUSNonSIMpullReel(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381497
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelOverRestrictions()
        sleep(3)
        self.circuits.createLargeUSCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        package = self.reels.getReelPackage()

        self.assertion.assertEqual(package, 'A62R')

    @pytest.mark.ac
    def testLargestProductIsCorrectWhenHeightIsTheLimitingFactor(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381502
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithHeightRestrictionOf31()
        sleep(3)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getExceedsAlert()
        package = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithWidthRestrictionOf21()
        sleep(3)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getExceedsAlert()
        package = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithWeightRestrictionOf1000()
        sleep(3)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getExceedsAlert()
        package = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'C17')
        self.assertion.assertEqual(weight, '58%')
        self.assertion.assertEqual(volume, '80%')

    @pytest.mark.ac
    def testReelSizeIncreaseBy2WhenExceedCurrentVolumeCapacity(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381513
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createMediumUSCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'C17')
        self.assertion.assertEqual(weight, '58%')
        self.assertion.assertEqual(volume, '80%')

    @pytest.mark.ac
    def testReelSizeIncreaseBy2WhenExceedCurrentVolumeCapacity(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381518
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeCACircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createSIMpullReelWithNoRestriction()
        sleep(3)
        oldValue = self.reels.getReelPackage()
        self.circuits.createLargeCASIMpullCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, '61"')
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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createMiniUSCircuit()
        sleep(2)
        self.circuits.createMiniUSCircuit()
        sleep(2)
        self.circuits.createMiniUSCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        # end of precondition
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        self.feederSchedule.confirmRemoval()
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeUSCircuit()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        # end of precondition
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        self.feederSchedule.confirmRemoval()
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeCACircuit()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        # end of precondition
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        self.feederSchedule.confirmRemoval()
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createSIMpullReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeCASIMpullCircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        sleep(2)
        self.feederSchedule.confirmRemoval()
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

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
        self.projects.selectAProject()
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(3)
        self.circuits.createLargeCACircuit()
        sleep(2)
        self.circuits.createLargeCACircuit()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldValue = self.reels.getReelPackage()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.getExceedsAlert()
        newValue = self.reels.getReelPackage()
        weight = self.reels.getWeightPercentage()
        volume = self.reels.getVolumePercentage()

        self.assertion.assertEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, 'A62R')
        self.assertion.assertEqual(weight, '94%')
        self.assertion.assertEqual(volume, '96%')




