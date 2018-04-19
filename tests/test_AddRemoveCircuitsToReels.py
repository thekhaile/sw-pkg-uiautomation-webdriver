from time import sleep
import pytest
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.job import Job


class TestAddRemoveCircuitsToReel(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestAddRemoveCircuitsToReel, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reel = Reel(self)
        self.circuit = Circuit(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)

    @pytest.mark.ac
    def testCircuitCannotBeAddedToReelWhenNoReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381436
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.circuit.createSmallCircuit()
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
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createSIMpullReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        oldValue = self.feederSchedule.getCircuitFrom()
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.feederSchedule.getNumberOfRows()
        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom()

        self.assertion.assertEqual(oldValue,newValue)

    @pytest.mark.ac
    def testAddCircuitToNoneSIMpullReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381438
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        oldValue = self.feederSchedule.getCircuitFrom()
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.feederSchedule.getNumberOfRows()
        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom()

        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testGreenCannotBeAddedToReelWithOtherColors(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381442
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createGreenCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        alert = self.feederSchedule.getIncompatibleAlert()
        newRowNumber = self.feederSchedule.getNumberOfRows()

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
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        # end of precondition
        self.circuit.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)

    @pytest.mark.ac
    def testDifferentColorCircuitsCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381444
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createCircuitOfDifferentColors()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)

    @pytest.mark.ac
    def testGreenCircuitOfDifferentSizeCannotBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381445
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createGreenCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        self.circuit.createGreenCircuitOfDifferentSize()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getIncompatibleAlert()
        newRowNumber = self.feederSchedule.getNumberOfRows()

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
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        # end of precondition
        self.circuit.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)

    @pytest.mark.ac
    def testSameSizeCircuitsCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381447
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createSmallCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)

    @pytest.mark.ac
    def testDifferentSizeCircuitsCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381448
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createCircuitOfDifferentSize()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 1)

    @pytest.mark.ac
    def testGreenCircuitOfDifferentMetalInsulationCannotBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381449
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createGreenCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        self.circuit.createGreenCircuitOfDifferentMetalInsulation()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        alert = self.feederSchedule.getIncompatibleAlert()
        newRowNumber = self.feederSchedule.getNumberOfRows()

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
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        # end of precondition
        self.circuit.createGreenCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(3)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)

    @pytest.mark.ac
    def testCircuitWithSIMpullHeadCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381451
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createCircuitWithSIMpullHead()
        sleep(2)
        self.circuit.createCircuitWithSIMpullHead()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 2)

    @pytest.mark.ac
    def testCircuitWithoutSIMpullHeadCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381452
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 2)

    @pytest.mark.ac
    def testCircuitWithoutSIMpullHeadCanBeAddedOnSameReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381453
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        # end of precondition
        self.circuit.createSmallCircuit()
        sleep(2)
        self.circuit.createCircuitWithSIMpullHead()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber + 2)

    @pytest.mark.ac
    def testCircuitRemovedFromAReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381457
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        sleep(2)
        self.feederSchedule.confirmRemoval()
        sleep(2)
        self.feederSchedule.switchToAvailableCircuitTab()
        sleep(2)
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)

    @pytest.mark.ac
    def testCircuitRemovedCanBeReaddedToReel(self):
        email = 'ningxin.liao+testAddRemove@mutualmobile.com'
        password = 'password'

        self.caseId = 1381461
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        # precondition
        self.projectList.selectAProject()
        self.job.createAJob()
        sleep(3)
        self.jobList.selectAJob()
        sleep(3)
        self.jobSummary.tapConfigureJob()
        sleep(3)
        self.reel.createReelWithNoRestriction()
        sleep(2)
        self.circuit.createSmallCircuit()
        sleep(2)
        oldRowNumber = self.feederSchedule.getNumberOfRows()
        self.feederSchedule.tapAddCircuit()
        sleep(2)
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        self.feederSchedule.tapRemoveCircuit()
        sleep(2)
        self.feederSchedule.confirmRemoval()
        sleep(2)
        self.feederSchedule.switchToAvailableCircuitTab()
        sleep(2)
        # end of precondition
        self.feederSchedule.tapAddCircuit()
        self.feederSchedule.switchToCircuitsOnReelTab()
        newRowNumber = self.feederSchedule.getNumberOfRows()

        self.assertion.assertTrue(oldRowNumber, newRowNumber)


