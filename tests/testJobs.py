import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects
from southwire_pkg_uiautomation_webdriver.components.jobs import Jobs

class TestJobs(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestJobs, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)
        self.jobs = Jobs(self)

    @pytest.mark.sandbox
    def testCreateAJob(self):
        email = 'khai.le@mutualmobile.com'
        password = 'password'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(2)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('Test Job Name 123')
        sleep(2)
        self.jobs.enterWeight('5000')
        sleep(2)
        self.jobs.enterWidth('50')
        sleep(2)
        self.jobs.toggleSIMpullReel()
        sleep(2)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)



