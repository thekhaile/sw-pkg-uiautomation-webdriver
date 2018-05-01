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


class TestReel(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestReel, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)
        self.reel = Reel(self)
        self.jobSummary = JobSummary(self)
        self.jobList = JobList(self)
        self.reelList = ReelList(self)

    @pytest.mark.ac
    def testCreateReelWithUniqueNameAndToggleOn(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378402
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterRandomHeight()
        sleep(1)
        self.reel.enterRandomWidth()
        sleep(1)
        self.reel.enterRandomWeight()
        sleep(1)
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        sleep(1)
        el = self.reel.getSIMpullReelToggle()
        self.assertion.assertTrue(el.isOn())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithUniqueNameAndToggleOff(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378397
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterRandomHeight()
        sleep(1)
        self.reel.enterRandomWidth()
        sleep(1)
        self.reel.enterRandomWeight()
        sleep(1)
        toggle = self.reel.getSIMpullReelToggle()
        if toggle.isOn():
            self.reel.toggleSIMpullReel()
        sleep(1)
        el = self.reel.getSIMpullReelToggle()
        self.assertion.assertFalse(el.isOn())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithNewHeight(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378404
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterRandomHeight()
        sleep(1)
        self.reel.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithNewWidth(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378408
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterRandomWidth()
        sleep(1)
        self.reel.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithNewWeight(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378411
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterRandomWeight()
        sleep(1)
        self.reel.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testExitCreateReelProcess(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378861
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        sleep(1)
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterRandomWidth()
        sleep(1)
        self.reel.tapCancel()
        sleep(5)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    """Error handling"""
    @pytest.mark.ac
    def testCreateReelWithSameName(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378398
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        name = self.reel.generateRandomName()
        self.reel.enterReelName(name)
        sleep(1)
        self.reel.enterRandomWidth()
        sleep(1)
        self.reel.tapSubmit()
        sleep(3)
        self.reelList.tapCreateReel()
        sleep(1)
        currentUrl = self.driver.current_url
        self.reel.enterReelName(name)
        self.job.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Reel name already exists'
        actualErrorMsg = self.reel.getReelNameErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.reel.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    """Restrictions on Height, width, and weight"""
    @pytest.mark.ac
    def testCreateReelWithBelowLimitHeightforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1378421
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterHeight('76')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reel.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1378423
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWidth('50')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reel.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1378425
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWeight('22')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reel.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381258
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('77')
        sleep(1)
        self.reel.enterWidth('51')
        sleep(1)
        self.reel.enterWeight('23')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelAboveLimitHeightWidthWeightforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381259
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('80')
        sleep(1)
        self.reel.enterWidth('60')
        sleep(1)
        self.reel.enterWeight('50')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitHeightforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381255
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterHeight('29')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reel.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381256
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWidth('19')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reel.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381257
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWeight('49')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reel.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381260
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('30')
        sleep(1)
        self.reel.enterWidth('20')
        sleep(1)
        self.reel.enterWeight('50')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelAboveLimitHeightWidthWeightforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381261
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('40')
        sleep(1)
        self.reel.enterWidth('30')
        sleep(1)
        self.reel.enterWeight('80')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitHeightforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1378422
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterHeight('23')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reel.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1378424
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWidth('19')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reel.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1378426
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWeight('29')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reel.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381265
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('24')
        sleep(1)
        self.reel.enterWidth('20')
        sleep(1)
        self.reel.enterWeight('30')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelAboveLimitHeightWidthWeightforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381266
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('40')
        sleep(1)
        self.reel.enterWidth('30')
        sleep(1)
        self.reel.enterWeight('80')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitHeightforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381263
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterHeight('60')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reel.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381262
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWidth('50')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reel.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381264
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        self.reel.enterWeight('13')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reel.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381265
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('61')
        sleep(1)
        self.reel.enterWidth('51')
        sleep(1)
        self.reel.enterWeight('14')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(5)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelAboveLimitHeightWidthWeightforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381266
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('70')
        sleep(1)
        self.reel.enterWidth('60')
        sleep(1)
        self.reel.enterWeight('100')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitHeightforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1378415
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('50')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reel.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1378416
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterWidth('32')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reel.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1378417
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterWeight('729')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reel.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1381272
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('51')
        sleep(1)
        self.reel.enterWidth('33')
        sleep(1)
        self.reel.enterWeight('730')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelAboveLimitHeightWidthWeightforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1381271
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('70')
        sleep(1)
        self.reel.enterWidth('60')
        sleep(1)
        self.reel.enterWeight('900')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitHeightforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381267
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterHeight('129')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reel.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381268
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterWidth('81')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reel.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381270
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterWeight('331')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reel.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381269
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('130')
        sleep(1)
        self.reel.enterWidth('82')
        sleep(1)
        self.reel.enterWeight('332')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelAboveLimitHeightWidthWeightforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381273
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        """preconditions"""
        self.job.createAJob()
        """end of preconditions"""
        self.jobList.selectAJob()
        sleep(1)
        self.jobSummary.tapConfigureJob()
        sleep(1)
        self.reelList.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reel.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reel.toggleSIMpullReel()
        self.reel.enterRandomReelName()
        sleep(1)
        self.reel.enterHeight('200')
        sleep(1)
        self.reel.enterWidth('100')
        sleep(1)
        self.reel.enterWeight('888')
        sleep(1)
        el = self.reel.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reel.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)








