from time import sleep
import pytest
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.configurator.feederSchedule import FeederSchedule
from southwire_pkg_uiautomation_webdriver.components.job import Job
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.project import Project
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.configurator.reelList import ReelList
from southwire_pkg_uiautomation_webdriver.components.reel import Reel
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary
from southwire_pkg_uiautomation_webdriver.components.circuit import Circuit
from southwire_pkg_uiautomation_webdriver.components.requestQuote import RequestQuote
from southwire_pkg_uiautomation_webdriver.components.jobSummary.reels import Reels



class TestDuplicateJob(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestDuplicateJob, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobSummary = JobSummary(self)
        self.reel = Reel(self)
        self.project = Project(self)
        self.circuit = Circuit(self)
        self.requestQuote = RequestQuote(self)
        self.reels = Reels(self)

    @pytest.mark.ac
    def testDuplicatedJobHasIdenticalSettings(self):
        # Verify the duplicated job's settings are identical to the original
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388781
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterJobName(self.job.generateRandomName())
        self.job.enterHeight("1000")
        self.job.enterWidth("1000")
        self.job.enterWeight("1000")
        simpullToggle = self.job.getSIMpullReelToggle().getValue()
        self.job.tapSubmit()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapEditSettings()
        sleep(1)
        height = self.job.getHeight()
        width = self.job.getWidth()
        weight = self.job.getWeight()

        self.assertion.assertEqual('1000', height)
        self.assertion.assertEqual('1000', width)
        self.assertion.assertEqual('1000', weight)
        self.assertion.assertEqual(simpullToggle, self.job.getSIMpullReelToggle().getValue())

    @pytest.mark.ac
    def testDuplicatedJobHasIdenticalReelsInfo(self):
        # Verify the duplicated job's reels are identical to the original
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388785
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        sleep(1)
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        for i in range(2):
            self.reelList.tapCreateReel()
            self.reel.enterRandomReelName()
            self.reel.tapSubmit()
        reelList = self.reelList.getReels()
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        self.jobList.selectAJob()
        self.jobSummary.tapConfigureJob()
        newReelList = self.reelList.getReels()

        self.assertion.assertEqual(reelList, newReelList)

    @pytest.mark.ac
    def testJobCountIncreaseByOneAfterAJobHasBeenDuplicated(self):
        # Verify the list of jobs is incremented after duplication
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388791
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterRandomJobName()
        self.job.tapSubmit()
        sleep(1)
        jobCount = self.jobList.getJobCount()
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        newJobCount = self.jobList.getJobCount()

        self.assertion.assertEqual(jobCount + 1, newJobCount)

    @pytest.mark.ac
    def testDuplicatedJobIsOnTheTopOfTheList(self):
        # Verify the duplicated job is placed at the top of the job list
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388790
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        self.job.enterJobName(self.job.generateRandomName())
        self.job.tapSubmit()
        sleep(1)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        newJobName = self.job.generateRandomName()
        self.job.enterJobName(newJobName)
        self.job.tapSubmit()
        sleep(1)
        recentJobName = self.jobList.getJobName(rowOrder=0)

        self.assertion.assertEqual(newJobName, recentJobName)

    @pytest.mark.ac
    def testDuplicatedJobWithNonUniqueName(self):
        # Verify when a non-unique job name is added that an error appears
        email = 'nick.moore+auto1@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1388773
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapCreateJob()
        jobName = self.job.generateRandomName()
        self.job.enterJobName(jobName)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(1)
        self.jobList.tapDuplicateJob()
        sleep(1)
        self.job.enterJobName(jobName)
        self.job.tapSubmit()
        expectedErrorMsg = 'Job name already exists.'
        actualErrorMsg = self.job.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)

    @pytest.mark.ac
    def testDuplicateButtonIsEnabledForInprogressJob(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388770
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        el = self.jobList.getDuplicateJobButton()
        self.assertion.assertExists(el.ui_object)

    @pytest.mark.ac
    def testDuplicateButtonIsEnabledForJobSubmittedForRFQ(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388771
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        '''precondition'''
        self.project.createAProject()
        sleep(2)
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
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(3)
        self.requestQuote.tapSubmit()
        sleep(2)
        '''end of precondition'''
        self.navigation.navigateToProjectsPage()
        sleep(2)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        el = self.jobList.getDuplicateJobButton()
        self.assertion.assertExists(el.ui_object)

    @pytest.mark.ac
    def testWhenTappingOnDuplicateJobTransitionsToDuplicateJobScreen(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388772
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDuplicateJob()
        sleep(2)
        newUrl = self.driver.current_url
        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testErrorMessageDisplayedWhenEnterMoreThan30CharOnDuplicateJobScreen(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388775
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDuplicateJob()
        sleep(2)
        self.job.enterJobName('Test Job Name Over 30 Characters')
        sleep(2)
        el = self.job.getErrorMsg()
        self.assertion.assertEqual(el, 'Job name cannot exceed 30 characters.')

    @pytest.mark.ac
    def testSubmitButtonIsDisabledWhenNameFieldIsEmptyOnDuplicateJobScreen(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'

        self.caseId = 1388776
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.job.createAJob()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDuplicateJob()
        sleep(2)
        el = self.job.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testDuplicatedJobHasANewCreatedDate(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388779
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        oldValue = self.jobList.getJobCreatedDate(rowOrder=-1)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        newValue = self.jobList.getJobCreatedDate()
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testDuplicatedJobHasAnEmptyModifiedDate(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388780
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        oldValue = self.jobList.getJobModifiedDate(rowOrder=-1)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        newValue = self.jobList.getJobModifiedDate()
        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, '')

    @pytest.mark.ac
    def testJobsiteRestrictionCanBeEditedForDuplicatedJob(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388782
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        oldValue = self.job.getHeight()
        self.job.enterHeight('100')
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapEditSettings()
        sleep(2)
        newValue = self.job.getHeight()
        self.assertion.assertNotEqual(oldValue, newValue)
        self.assertion.assertEqual(newValue, '100')

    @pytest.mark.ac
    def testDuplicatedJobSharesTheSameFeederSchedule(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388783
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.selectAJob(rowOrder=-1)
        sleep(2)
        oldValue = self.feederSchedule.getCircuitTo()
        self.navigation.navigateToProjectsPage()
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        newValue = self.feederSchedule.getCircuitTo()
        self.assertion.assertEqual(oldValue, newValue)

    @pytest.mark.ac
    def testFeederScheduleCanBeEditedOnDuplicatedJob(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388784
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        self.feederSchedule.switchToCircuitsOnReelTab()
        sleep(2)
        oldValue = self.feederSchedule.getCircuitFrom()
        self.feederSchedule.tapRemoveCircuit()
        self.feederSchedule.confirmRemoval()
        sleep(2)
        self.feederSchedule.switchToAvailableCircuitTab()
        sleep(2)
        self.feederSchedule.tapOverflow()
        sleep(2)
        self.feederSchedule.tapEditCircuit()
        self.circuit.enterRandomFrom()
        sleep(2)
        self.circuit.tapSubmit()
        sleep(2)
        newValue = self.feederSchedule.getCircuitFrom()
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testReelConfiguratorCanBeEditedOnDuplicatedJob(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388786
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapConfigureJob()
        sleep(2)
        oldValue = self.reelList.getReelName()
        self.reelList.tapOverflow()
        sleep(2)
        self.reelList.tapEditReel()
        self.reel.enterRandomReelName()
        sleep(2)
        self.reel.tapSubmit()
        sleep(2)
        newValue = self.reelList.getReelName()
        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testDuplicatedJobCanBeDeleted(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388787
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        oldJobCount = self.jobList.getJobCount()
        jobName = self.jobList.getJobName(rowOrder=0)
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDeleteJob()
        sleep(2)
        self.jobList.tapConfirmDelete()
        sleep(2)
        newJobCount = self.jobList.getJobCount()
        self.assertEqual(oldJobCount - 1, newJobCount)
        if newJobCount >= 1:
            newJobName = self.jobList.getJobName(rowOrder=0)
            self.assertion.assertNotEqual(jobName, newJobName)

    @pytest.mark.ac
    def testDuplicatedJobCanBeDuplicatedAgain(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388788
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        oldJobCount = self.jobList.getJobCount()
        self.jobList.tapOverflow()
        sleep(2)
        self.jobList.tapDuplicateJob()
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        newJobCount = self.jobList.getJobCount()
        self.assertEqual(oldJobCount, newJobCount - 1)

    @pytest.mark.ac
    def testDuplicatedJobCanBeSubmittedForRFQ(self):
        email = 'ningxin.liao+test2@mutualmobile.com'
        password = 'password'

        self.caseId = 1388793
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        sleep(2)
        self.jobList.tapOverflow(rowOrder=-1)
        sleep(2)
        self.jobList.tapDuplicateJob(rowOrder=-1)
        sleep(2)
        self.job.enterRandomJobName()
        sleep(2)
        self.job.tapSubmit()
        sleep(2)
        self.jobList.selectAJob()
        sleep(2)
        self.jobSummary.tapRequestQuote()
        sleep(2)
        self.requestQuote.tapSubmit()
        sleep(2)
        self.assertion.assertExists(self.jobSummary.getQuoteSubmittedDate())
