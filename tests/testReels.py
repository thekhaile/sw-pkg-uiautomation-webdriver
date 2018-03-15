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
    def testCreateReelWithWithUniqueNameAndToggleOn(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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
        self.reels.toggleSIMpullReel()
        sleep(1)
        el = self.reels.getSIMpullReelToggle()
        self.assertion.assertTrue(el.isOn())
        self.reels.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testCreateReelWithWithUniqueNameAndToggleOff(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        name = self.reels.getRandomName()
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

    @pytest.mark.ac
    def testCreateReelWithErrorHeight(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(1)
        self.jobs.tapConfigureJob()
        sleep(1)
        self.feederSchedule.tapCreateReel()
        currentUrl = self.driver.current_url
        self.reels.enterRandomReelName()
        sleep(1)
        self.reels.enterHeight('6')
        sleep(1)
        self.reels.enterRandomWidth()
        sleep(1)
        self.reels.enterRandomWeight()
        sleep(1)
        el = self.reels.getSIMpullReelToggle()
        self.assertion.assertFalse(el.isOn())
        self.reels.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'No reel available'
        actualErrorMsg = self.reels.getHeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.reels.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateReelWithErrorWidth(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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
        self.reels.enterWidth('6')
        sleep(1)
        self.reels.enterRandomWeight()
        sleep(1)
        el = self.reels.getSIMpullReelToggle()
        self.assertion.assertFalse(el.isOn())
        self.reels.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'No reel available'
        actualErrorMsg = self.reels.getWidthErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.reels.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())

    @pytest.mark.ac
    def testCreateReelWithErrorWeight(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
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
        self.reels.enterWeight('6')
        sleep(1)
        el = self.reels.getSIMpullReelToggle()
        self.assertion.assertFalse(el.isOn())
        self.reels.tapSubmit()
        sleep(3)
        newUrl = self.driver.current_url
        expectedErrorMsg = 'No reel available'
        actualErrorMsg = self.reels.getWeightErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)
        self.assertion.assertEqual(currentUrl, newUrl)

        el = self.reels.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())







