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

class TestReels(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestReels, self).__init__(*args, **kwargs)
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