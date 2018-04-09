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

    def testAddCircuitToReel(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.selectAJob()
        sleep(3)
        self.jobs.tapConfigureJob()
        sleep(3)
        self.reels.createReelWithNoRestriction()
        self.circuits.createCircuit()
        sleep(3)