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

    @pytest.mark.ac1
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
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac2
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
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac3
    def testCreateReelWithNewHeightWidthAndWeight(self):
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
        self.reels.toggleSIMpullReel()
        sleep(1)
        self.reels.tapSubmit()
        sleep(1)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)


