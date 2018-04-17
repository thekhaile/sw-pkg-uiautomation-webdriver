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
    def testCreateReelWithUniqueNameAndToggleOn(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378402
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterRandomHeight()
        sleep(1)
        self.reels.enterRandomWidth()
        sleep(1)
        self.reels.enterRandomWeight()
        sleep(1)
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        sleep(1)
        el = self.reels.getSIMpullReelToggle()
        self.assertion.assertTrue(el.isOn())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterRandomHeight()
        sleep(1)
        self.reels.enterRandomWidth()
        sleep(1)
        self.reels.enterRandomWeight()
        sleep(1)
        toggle = self.reels.getSIMpullReelToggle()
        if toggle.isOn():
            self.reels.toggleSIMpullReel()
        sleep(1)
        el = self.reels.getSIMpullReelToggle()
        self.assertion.assertFalse(el.isOn())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterRandomHeight()
        sleep(1)
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterRandomWidth()
        sleep(1)
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterRandomWeight()
        sleep(1)
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        sleep(1)
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterRandomWidth()
        sleep(1)
        self.reels.tapCancel()
        sleep(5)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    # Error handling
    @pytest.mark.ac
    def testCreateReelWithSameName(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1378398
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        name = self.reels.generateRandomName()
        self.reels.enterReelName(name)
        sleep(1)
        self.reels.enterRandomWidth()
        sleep(1)
        self.reels.tapSubmit()
        sleep(3)
        self.feederSchedule.tapCreateReel()
        sleep(1)
        currentUrl = self.driver.current_url
        self.reels.enterReelName(name)
        self.jobs.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'Reel name already exists'
        actualErrorMsg = self.reels.getReelNameErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.reels.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    # restrictions on Height, width, and weight #
    @pytest.mark.ac
    def testCreateReelWithBelowLimitHeightforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1378421
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterHeight('76')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reels.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1378423
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWidth('50')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reels.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1378425
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWeight('22')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reels.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforUSinMetric(self):
        email = 'ningxin.liao+USinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381258
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('77')
        sleep(1)
        self.reels.enterWidth('51')
        sleep(1)
        self.reels.enterWeight('23')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('80')
        sleep(1)
        self.reels.enterWidth('60')
        sleep(1)
        self.reels.enterWeight('50')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterHeight('29')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reels.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381256
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWidth('19')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reels.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381257
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWeight('49')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reels.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforUSinStandard(self):
        email = 'ningxin.liao+USinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381260
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('30')
        sleep(1)
        self.reels.enterWidth('20')
        sleep(1)
        self.reels.enterWeight('50')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('40')
        sleep(1)
        self.reels.enterWidth('30')
        sleep(1)
        self.reels.enterWeight('80')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterHeight('23')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reels.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1378424
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWidth('19')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reels.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1378426
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWeight('29')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reels.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforCAinStandard(self):
        email = 'ningxin.liao+CAinStd@mutualmobile.com'
        password = 'password'

        self.caseId = 1381265
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('24')
        sleep(1)
        self.reels.enterWidth('20')
        sleep(1)
        self.reels.enterWeight('30')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('40')
        sleep(1)
        self.reels.enterWidth('30')
        sleep(1)
        self.reels.enterWeight('80')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterHeight('60')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reels.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381262
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWidth('50')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reels.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381264
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        self.reels.enterWeight('13')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reels.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforCAinMetric(self):
        email = 'ningxin.liao+CAinMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381265
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('61')
        sleep(1)
        self.reels.enterWidth('51')
        sleep(1)
        self.reels.enterWeight('14')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('70')
        sleep(1)
        self.reels.enterWidth('60')
        sleep(1)
        self.reels.enterWeight('100')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('50')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reels.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1378416
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterWidth('32')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reels.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1378417
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterWeight('729')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reels.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforSIMpullReelinStandard(self):
        email = 'ningxin.liao+SIMpullReestdl@mutualmobile.com'
        password = 'password'

        self.caseId = 1381272
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('51')
        sleep(1)
        self.reels.enterWidth('33')
        sleep(1)
        self.reels.enterWeight('730')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('70')
        sleep(1)
        self.reels.enterWidth('60')
        sleep(1)
        self.reels.enterWeight('900')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterHeight('129')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualHeightErrorMsg = self.reels.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualHeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWidthforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381268
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterWidth('81')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWidthErrorMsg = self.reels.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWidthErrorMsg)

    @pytest.mark.ac
    def testCreateReelWithBelowLimitWeightforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381270
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterWeight('331')
        sleep(6)
        expectedErrorMsg = 'No reel available'
        actualWeightErrorMsg = self.reels.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualWeightErrorMsg)

    @pytest.mark.ac
    def testCreateReelRightAtLimitHeightWidthWeightforSIMpullReelinMetric(self):
        email = 'ningxin.liao+SIMpullReelMetric@mutualmobile.com'
        password = 'password'

        self.caseId = 1381269
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('130')
        sleep(1)
        self.reels.enterWidth('82')
        sleep(1)
        self.reels.enterWeight('332')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
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
        self.projects.selectAProject()
        """preconditions"""
        self.jobs.createAJob()
        """end of preconditions"""
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        toggle = self.reels.getSIMpullReelToggle()
        if not toggle.isOn():
            self.reels.toggleSIMpullReel()
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('200')
        sleep(1)
        self.reels.enterWidth('100')
        sleep(1)
        self.reels.enterWeight('888')
        sleep(1)
        el = self.reels.getSubmitButton()
        self.assertion.assertTrue(el.isEnabled())
        self.reels.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testReelNameCanBeEdited(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381684
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """precondition"""
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        """end of precondition"""
        oldValue = self.reels.getReelName()
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapEditReel()
        sleep(2)
        self.reels.enterRandomReelName()
        sleep(2)
        self.reels.tapSubmit()
        sleep(2)
        newValue = self.reels.getReelName()

        self.assertion.assertNotEqual(oldValue, newValue)

    @pytest.mark.ac
    def testEditedReelNameCanNotBeTheSameAsOtherReels(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381685
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        """start of precondtion"""
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        self.feederSchedule.tapCreateReel()
        sleep(1)
        self.reels.enterReelName('Same Name')
        sleep(1)
        self.reels.tapSubmit()
        sleep(2)
        """end of precondtion"""
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapEditReel()
        sleep(2)
        self.reels.enterReelName('Same Name')
        sleep(2)
        self.reels.tapSubmit()
        sleep(2)
        errorMsg = self.reels.getReelNameErrorMsg()

        self.assertion.assertEqual(errorMsg, 'Reel name already exists.')

    @pytest.mark.ac
    def testEditedReelNameCanNotExceed30Char(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381686
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        # precondition
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        # end of precondition
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapEditReel()
        sleep(2)
        self.reels.enterReelName('OjHiHsYaHCTVyFe7UKmYyBX0Vwswjfdbs')
        sleep(2)
        self.reels.tapSubmit()
        sleep(2)
        errorMsg = self.reels.getReelNameErrorMsg()

        self.assertion.assertEqual(errorMsg, 'Reel name cannot exceed 30 characters.')

    @pytest.mark.ac
    def testSubmitButtonIsDisabledWhenNameFieldIsEmpty(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381687
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        # precondition
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        # end of precondition
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapEditReel()
        sleep(2)
        self.reels.enterReelName(' ')
        sleep(2)
        self.reels.tapSubmit()
        sleep(2)
        button = self.reels.getSubmitButton()

        self.assertion.assertFalse(button.isEnabled())

    @pytest.mark.ac
    def testSubmitButtonIsDisabledWhenThereIsAnError(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381690
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        # precondition
        self.jobs.createAJob()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.reels.createReelWithNoRestriction()
        sleep(2)
        # end of precondition
        self.reels.tapOverflow()
        sleep(2)
        self.reels.tapEditReel()
        sleep(2)
        self.reels.enterReelName('OjHiHsYaHCTVyFe7UKmYyBX0Vwswjfdbs')
        sleep(2)
        self.reels.tapSubmit()
        sleep(2)
        button = self.reels.getSubmitButton()

        self.assertion.assertFalse(button.isEnabled())






