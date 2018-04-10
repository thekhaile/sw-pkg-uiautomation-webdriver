__author__ = 'ningxinliao'
import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects
from southwire_pkg_uiautomation_webdriver.components.jobs import Jobs
from southwire_pkg_uiautomation_webdriver.components.reels import Reels
from southwire_pkg_uiautomation_webdriver.components.circuits import Circuits
from southwire_pkg_uiautomation_webdriver.components.feederSchedule import FeederSchedule
import unidecode

class TestCircuits(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestCircuits, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)
        self.jobs = Jobs(self)
        self.reels = Reels(self)
        self.circuits = Circuits(self)
        self.feederSchedule = FeederSchedule(self)

    @pytest.mark.ac
    def testCircuitCannotBeAddedToReelWhenNoReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381436
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.circuits.createSmallCircuit()
        sleep(3)
        add = self.feederSchedule.getAddButton()

        self.assertion.assertNotExists(add.ui_object)

    @pytest.mark.ac
    def testAddCircuitToSIMpullReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381437
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createSIMpullReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        oldValue = self.circuits.getCircuitFrom()
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.circuits.getNumberOfRows()
        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        newValue = self.circuits.getCircuitFrom()

        self.assertion.assertEqual(oldValue,newValue)

    @pytest.mark.ac
    def testAddCircuitToNoneSIMpullReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381438
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        oldValue = self.circuits.getCircuitFrom()
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.circuits.getNumberOfRows()
        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        newValue = self.circuits.getCircuitFrom()

        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testGreenCannotBeAddedToReelWithOtherColors(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381442
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createGreenCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        alert = self.feederSchedule.getIncompatibleAlert()
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)
        self.assertion.assertExists(alert.ui_object)

    @pytest.mark.ac
    def testGreenCircuitOfSameColorCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381443
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        # end of precondition
        self.circuits.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)

    @pytest.mark.ac
    def testDifferentColorCircuitsCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381444
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createCircuitOfDifferentColors()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)

    @pytest.mark.ac
    def testGreenCircuitOfDifferentSizeCannotBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381445
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createGreenCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        self.circuits.createGreenCircuitOfDifferentSize()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getIncompatibleAlert()
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)
        self.assertion.assertExists(alert.ui_object)

    @pytest.mark.ac
    def testGreenCircuitOfSameSizeCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381446
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        # end of precondition
        self.circuits.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)

    @pytest.mark.ac
    def testSameSizeCircuitsCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381447
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)

    @pytest.mark.ac
    def testDifferentSizeCircuitsCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381448
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createCircuitOfDifferentSize()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)

    @pytest.mark.ac
    def testGreenCircuitOfDifferentMetalInsulationCannotBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381449
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuits.createGreenCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        self.circuits.createGreenCircuitOfDifferentMetalInsulation()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getIncompatibleAlert()
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)
        self.assertion.assertExists(alert.ui_object)

    @pytest.mark.ac
    def testGreenCircuitOfSameMetalInsulationCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381450
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projects.selectAProject()
        self.jobs.createAJob()
        sleep(3)
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.circuits.createSmallCircuit()
        sleep(2)
        self.circuits.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldRowNumber = self.circuits.getNumberOfRows()
        # end of precondition
        self.circuits.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.circuits.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)
