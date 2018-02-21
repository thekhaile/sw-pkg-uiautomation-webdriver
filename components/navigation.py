from time import sleep
from projectBase import ProjectBase

class Navigation(object):
    LOGIN_PAGE = 'https://southwire-configurator-test.firebaseapp.com/login'
    PROJECTS_PAGE= 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testc=Case: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def navigateToLoginPage(self):
        self.testCase.driver.get(Navigation.LOGIN_PAGE)

    def navigateToProjectsPage(self):
        self.testCase.driver.get(Navigation.PROJECTS_PAGE)