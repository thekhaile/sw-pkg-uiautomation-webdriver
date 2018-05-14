__author__ = 'ningxinliao'
from time import sleep
import pytest
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit

class TestSortCircuit(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestSortCircuit, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.jobSummary = JobSummary(self)
        self.feederSchedule = FeederSchedule(self)
        self.circuit = Circuit(self)

    @pytest.mark.ac
    # Verify that the feeder schedule is sort by most recently created by default
    def testDefaultSortingIsMostRecentlyCreated(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1376417
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(2)
        '''Precondition'''
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('A')
        self.circuit.enterTo('B')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('1')
        self.circuit.enterCircuitLength('300')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('E')
        self.circuit.enterTo('F')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('300')
        self.circuit.enterCircuitLength('100')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('C')
        self.circuit.enterTo('D')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('6')
        self.circuit.enterCircuitLength('500')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Brown-Orange-Yellow')
        self.circuit.tapSubmit()
        sleep(5)
        '''End of precondition'''
        fromList = ['C', 'E', 'A']
        toList = ['D', 'F', 'B']
        sizeList = ['6', '300', '1']
        lengthList = ['500m', '100m', '300m']

        for i in range(3):
            self.assertion.assertEqual(self.feederSchedule.getCircuitFrom(i), fromList[i],
                                       "Circuit FROM does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitTo(i), toList[i], "Circuit TO does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitSize(i), sizeList[i],
                                       "Circuit SIZE does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitLength(i), lengthList[i],
                                       "Circuit LENGTH does not match")

    @pytest.mark.ac
    # Verify that tapping on From button on feeder schedule screen is sorting the from field in ascending order
    def testSortByFrom(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1376429
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(2)
        '''Precondition'''
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('A')
        self.circuit.enterTo('B')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('1')
        self.circuit.enterCircuitLength('300')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('E')
        self.circuit.enterTo('F')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('300')
        self.circuit.enterCircuitLength('100')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('C')
        self.circuit.enterTo('D')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('6')
        self.circuit.enterCircuitLength('500')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Brown-Orange-Yellow')
        self.circuit.tapSubmit()
        sleep(5)
        '''End of precondition'''
        self.feederSchedule.tapSortByFrom()
        sleep(2)
        fromList = ['A', 'C', 'E']
        toList = ['B', 'D', 'F']
        sizeList = ['1', '6', '300']
        lengthList = ['300m', '500m', '100m']

        for i in range(3):
            self.assertion.assertEqual(self.feederSchedule.getCircuitFrom(i), fromList[i],
                                       "Circuit FROM does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitTo(i), toList[i], "Circuit TO does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitSize(i), sizeList[i],
                                       "Circuit SIZE does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitLength(i), lengthList[i],
                                       "Circuit LENGTH does not match")

    @pytest.mark.ac
    # Verify that tapping on To button on feeder schedule screen is sorting the To field in ascending order
    def testSortByTo(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1376431
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(2)
        '''Precondition'''
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('A')
        self.circuit.enterTo('B')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('1')
        self.circuit.enterCircuitLength('300')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('E')
        self.circuit.enterTo('F')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('300')
        self.circuit.enterCircuitLength('100')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('C')
        self.circuit.enterTo('D')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('6')
        self.circuit.enterCircuitLength('500')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Brown-Orange-Yellow')
        self.circuit.tapSubmit()
        sleep(5)
        '''End of precondition'''
        self.feederSchedule.tapSortByTo()
        sleep(2)
        fromList = ['A', 'C', 'E']
        toList = ['B', 'D', 'F']
        sizeList = ['1', '6', '300']
        lengthList = ['300m', '500m', '100m']

        for i in range(3):
            self.assertion.assertEqual(self.feederSchedule.getCircuitFrom(i), fromList[i],
                                       "Circuit FROM does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitTo(i), toList[i], "Circuit TO does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitSize(i), sizeList[i],
                                       "Circuit SIZE does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitLength(i), lengthList[i],
                                       "Circuit LENGTH does not match")

    @pytest.mark.ac
    # Verify that tapping on Length button on feeder schedule screen is sorting the Length field in ascending order
    def testSortByLength(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1376433
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(2)
        '''Precondition'''
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('A')
        self.circuit.enterTo('B')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('1')
        self.circuit.enterCircuitLength('300')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('E')
        self.circuit.enterTo('F')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('300')
        self.circuit.enterCircuitLength('100')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('C')
        self.circuit.enterTo('D')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('6')
        self.circuit.enterCircuitLength('500')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Brown-Orange-Yellow')
        self.circuit.tapSubmit()
        sleep(5)
        '''End of precondition'''
        self.feederSchedule.tapSortByLength()
        sleep(2)
        fromList = ['E', 'A', 'C']
        toList = ['F', 'B', 'D']
        sizeList = ['300', '1', '6']
        lengthList = ['100m', '300m', '500m']

        for i in range(3):
            self.assertion.assertEqual(self.feederSchedule.getCircuitFrom(i), fromList[i],
                                       "Circuit FROM does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitTo(i), toList[i], "Circuit TO does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitSize(i), sizeList[i],
                                       "Circuit SIZE does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitLength(i), lengthList[i],
                                       "Circuit LENGTH does not match")

    @pytest.mark.ac
    # Verify that tapping on Size button on feeder schedule screen is sorting the Size field in ascending order
    def testSortBySize(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1376435
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(2)
        '''Precondition'''
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('A')
        self.circuit.enterTo('B')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('1')
        self.circuit.enterCircuitLength('300')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('E')
        self.circuit.enterTo('F')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('300')
        self.circuit.enterCircuitLength('100')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('C')
        self.circuit.enterTo('D')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('6')
        self.circuit.enterCircuitLength('500')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Brown-Orange-Yellow')
        self.circuit.tapSubmit()
        sleep(5)
        '''End of precondition'''
        self.feederSchedule.tapSortBySize()
        sleep(2)
        fromList = ['C', 'A', 'E']
        toList = ['D', 'B', 'F']
        sizeList = ['6', '1', '300']
        lengthList = ['500m', '300m', '100m']

        for i in range(3):
            self.assertion.assertEqual(self.feederSchedule.getCircuitFrom(i), fromList[i],
                                       "Circuit FROM does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitTo(i), toList[i], "Circuit TO does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitSize(i), sizeList[i],
                                       "Circuit SIZE does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitLength(i), lengthList[i],
                                       "Circuit LENGTH does not match")

    @pytest.mark.ac
    # Verify that when refreshing the page, the currently selected sorting persists
    def testSortPersistWhenRefreshPage(self):
        email = 'ningxin.liao+regression4@mutualmobile.com'
        password = 'password'

        self.caseId = 1376426
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.jobList.selectAJob()
        sleep(2)
        '''Precondition'''
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('A')
        self.circuit.enterTo('B')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('1')
        self.circuit.enterCircuitLength('300')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Red-Blue')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('E')
        self.circuit.enterTo('F')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('300')
        self.circuit.enterCircuitLength('100')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Black-Black-Black')
        self.circuit.tapSubmit()
        sleep(2)
        self.feederSchedule.tapCreateCircuit()
        sleep(2)
        self.circuit.enterFrom('C')
        self.circuit.enterTo('D')
        self.circuit.selectConductorType('CU / RW90')
        self.circuit.selectConductorSize('6')
        self.circuit.enterCircuitLength('500')
        self.circuit.selectNumOfConductor('3')
        self.circuit.selectCommonPreset('Brown-Orange-Yellow')
        self.circuit.tapSubmit()
        sleep(5)
        '''End of precondition'''
        self.feederSchedule.tapSortBySize()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        fromList = ['C', 'A', 'E']
        toList = ['D', 'B', 'F']
        sizeList = ['6', '1', '300']
        lengthList = ['500m', '300m', '100m']

        for i in range(3):
            self.assertion.assertEqual(self.feederSchedule.getCircuitFrom(i), fromList[i],
                                       "Circuit FROM does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitTo(i), toList[i], "Circuit TO does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitSize(i), sizeList[i],
                                       "Circuit SIZE does not match")
            self.assertion.assertEqual(self.feederSchedule.getCircuitLength(i), lengthList[i],
                                       "Circuit LENGTH does not match")



