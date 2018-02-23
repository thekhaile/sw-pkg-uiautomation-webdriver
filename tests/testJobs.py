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

    @pytest.mark.nx
    def testCreateJobWithUniqueNmaeAndToggleOn(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        # currentUrl = self.driver.current_url
        self.jobs.enterJobName('Ningxin 3rd Automation Job')
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(2)
        self.jobs.enterHeight('999')
        sleep(2)
        self.jobs.enterWidth('66')
        sleep(2)
        self.jobs.toggleSIMpullReel()
        sleep(2)
        self.jobs.tapSubmit()
        sleep(2)
        # newUrl = self.driver.current_url

        #self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.nxTest
    def testCreateJobWithUniqueNmaeAndToggleOff(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        # currentUrl = self.driver.current_url
        self.jobs.enterJobName('Ningxin 1st Automation Job')
        sleep(1)
        self.jobs.enterWeight('99')
        sleep(2)
        self.jobs.enterHeight('88')
        sleep(2)
        self.jobs.enterWidth('66')
        sleep(2)
        # self.jobs.toggleSIMpullReel()
        # sleep(2)
        self.jobs.tapSubmit()
        sleep(2)
        # newUrl = self.driver.current_url

        # self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.nxTest
    def testCreateJobWithoutUniqueNmae(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('Ningxin 2nd Automation Job')
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(2)
        self.jobs.enterHeight('999')
        sleep(2)
        self.jobs.enterWidth('66')
        sleep(2)
        self.jobs.toggleSIMpullReel()
        sleep(2)
        self.jobs.tapSubmit()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)

    @pytest.mark.nxTest2
    def testCreateJobWithOver30CharLimit(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('abc def ghi jkl mno pqrs tuv w1')
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(2)
        self.jobs.enterHeight('999')
        sleep(2)
        # self.jobs.enterWidth('66')
        # sleep(2)
        # self.jobs.toggleSIMpullReel()
        # sleep(2)
        # self.jobs.tapSubmit()
        # sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertEqual(currentUrl, newUrl)


    @pytest.mark.nxTest
    def testExitCreateJobProcess(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.selectAProject()
        self.jobs.tapCreateJob()
        sleep(1)
        currentUrl = self.driver.current_url
        self.jobs.enterJobName('Ningxin 2nd Automation Job')
        sleep(1)
        self.jobs.enterWeight('88')
        sleep(2)
        # self.jobs.enterHeight('999')
        # sleep(2)
        # self.jobs.enterWidth('66')
        # sleep(2)
        # self.jobs.toggleSIMpullReel()
        # sleep(2)
        self.jobs.tapCancel()
        sleep(2)
        newUrl = self.driver.current_url

        # self.assertion.assertEqual(currentUrl, newUrl)


